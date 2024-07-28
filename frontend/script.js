async function getRecommendations() {
    const userId = document.getElementById('user-id').value;

    if (!userId.trim()) {
        alert('Please enter a user ID.');
        return;
    }

    try {
        const response = await fetch('http://127.0.0.1:5000/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_id: userId })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const recommendations = data.recommendations;
        const recommendationsDiv = document.getElementById('recommendations');

        if (recommendations.length === 0) {
            recommendationsDiv.innerHTML = 'No recommendations available.';
        } else {
            recommendationsDiv.innerHTML = 'Recommended Movies:<ul>' + 
                recommendations.map(movie => `<li>${movie}</li>`).join('') + 
                '</ul>';
        }
    } catch (error) {
        console.error('Error fetching recommendations:', error);
        document.getElementById('recommendations').innerHTML = 'Error fetching recommendations.';
    }
}
