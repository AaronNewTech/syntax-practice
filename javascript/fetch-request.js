const fetchLaunchData = async () => {
    try {
        const response = await fetch('https://api.spacexdata.com/v4/launches')
        if (response.ok) {
            const data = await response.json()
            console.log(data)
        }
        else {
            console.error('Failed to fetch launch data: ' + response.status)
        } 
    }
        catch (error) {
            console.error('Failed to fetch launch data: ', error)
        }
    
}

fetchLaunchData()