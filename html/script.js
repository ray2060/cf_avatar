// Codeforces ranks with their colors and font sizes
const RANKS = {
    'newbie': {
        color: [128, 128, 128],      // Gray
        fontSize: 36
    },
    'pupil': {
        color: [0, 128, 0],          // Green
        fontSize: 36
    },
    'specialist': {
        color: [3, 168, 158],        // Cyan
        fontSize: 36
    },
    'expert': {
        color: [0, 0, 255],          // Blue
        fontSize: 36
    },
    'candidate master': {
        color: [170, 0, 170],        // Purple
        fontSize: 36
    },
    'master': {
        color: [255, 140, 0],        // Orange
        fontSize: 36
    },
    'international master': {
        color: [255, 140, 0],        // Orange
        fontSize: 36
    },
    'grandmaster': {
        color: [255, 0, 0],          // Red
        fontSize: 36
    },
    'international grandmaster': {
        color: [255, 0, 0],          // Red
        fontSize: 30
    },
    'legendary grandmaster': {
        color: [192, 64, 64],        // Dark Red
        fontSize: 36
    }
};

// DOM elements
const usernameInput = document.getElementById('username');
const generateBtn = document.getElementById('generate-btn');
const downloadBtn = document.getElementById('download-btn');
const canvas = document.getElementById('avatar-canvas');
const ctx = canvas.getContext('2d');

// Load font
let iosevkaFont = new FontFace('Iosevka Bold', 'url(fonts/Iosevka-Bold.ttc)');
iosevkaFont.load().then(function(loadedFont) {
    document.fonts.add(loadedFont);
}).catch(function(error) {
    console.log('Failed to load custom font, using default font instead');
});

// Event listeners
generateBtn.addEventListener('click', generateAvatar);
downloadBtn.addEventListener('click', downloadAvatar);

// Get color by rank
function getColorByRank(rank) {
    const normalizedRank = rank.toLowerCase();
    return RANKS[normalizedRank]?.color || [0, 0, 0];
}

// Get font size by rank
function getFontSizeByRank(rank) {
    const normalizedRank = rank.toLowerCase();
    return RANKS[normalizedRank]?.fontSize || 36;
}

// Fetch user data from Codeforces API
async function fetchUserData(username) {
    try {
        const response = await fetch(`https://codeforces.com/api/user.info?handles=${username}`);
        const data = await response.json();
        
        if (data.status === 'OK') {
            return data.result[0];
        } else {
            throw new Error(data.comment || 'Unknown error');
        }
    } catch (error) {
        throw new Error(`Failed to fetch data: ${error.message}`);
    }
}

// Generate avatar on canvas
function drawAvatar(rank, rating, backgroundColor) {
    const width = canvas.width;
    const height = canvas.height;
    
    // Clear canvas
    ctx.clearRect(0, 0, width, height);
    
    // Fill background with white
    ctx.fillStyle = 'white';
    ctx.fillRect(0, 0, width, height);
    
    // Draw colored rectangle
    const rectHeight = height / 4;
    const rectY = (height - rectHeight) / 2;
    ctx.fillStyle = `rgb(${backgroundColor[0]}, ${backgroundColor[1]}, ${backgroundColor[2]})`;
    ctx.fillRect(0, rectY, width, rectHeight);
    
    // Set font and draw rank text
    const rankFontSize = getFontSizeByRank(rank);
    const useCustomFont = document.fonts.check('16px "Iosevka Bold"');
    const fontFace = useCustomFont ? 'Iosevka Bold' : 'monospace';
    
    ctx.font = `bold ${rankFontSize}px ${fontFace}`;
    ctx.fillStyle = 'white';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    
    const rankText = rank.toUpperCase();
    ctx.fillText(rankText, width/2, height/2 - rankFontSize/2);
    
    // Draw rating text
    ctx.font = `bold 36px ${fontFace}`;
    const ratingText = `${rating}`;
    ctx.fillText(ratingText, width/2, height/2 + 36/2);
}

// Generate avatar function
async function generateAvatar() {
    const username = usernameInput.value.trim();
    
    if (!username) {
        alert('Please enter a Codeforces username');
        return;
    }
    
    // Disable button and show loading
    generateBtn.disabled = true;
    generateBtn.innerHTML = '<span class="loading"></span> Generating...';
    
    try {
        // Fetch user data
        const userData = await fetchUserData(username);
        const rank = userData.rank || 'unrated';
        const rating = userData.rating || 0;
        const backgroundColor = getColorByRank(rank);
        
        // Draw avatar
        drawAvatar(rank, rating, backgroundColor);
        
        // Enable download button
        downloadBtn.disabled = false;
    } catch (error) {
        alert(`Error: ${error.message}`);
    } finally {
        // Re-enable button
        generateBtn.disabled = false;
        generateBtn.textContent = 'Generate Avatar';
    }
}

// Download avatar function
function downloadAvatar() {
    const link = document.createElement('a');
    link.download = `cf_avatar_${usernameInput.value.trim()}_${new Date().toISOString().slice(0, 19).replace(/:/g, '-')}.png`;
    link.href = canvas.toDataURL();
    link.click();
}
