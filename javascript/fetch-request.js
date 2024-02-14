// async function that waits for the user to complete the request
const fetchLaunchData = async () => {

    // try block to execute request
    try {

        // defining the request and capturing it in the response variable
        const response = await fetch('https://api.spacexdata.com/v4/launches');

        // check if response is successful and if not throw error with error message and response status
        if (!response.ok) {
            throw new Error('Failed to fetch launch data: ' + response.status);
        }
        
        // if response is successful parse the response body as JSON
        const data = await response.json();

        // print the launch data to the console
        console.log(data);
    }
    
    // log error console log error message if try block failed
    catch (error) {
        console.error('Failed to fetch launch data:', error);
    }
};

// function call
fetchLaunchData();
