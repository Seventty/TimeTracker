const axios = require('axios');
const data = require('endpoint.json');
 
axios
    .post('https://swift-penguin-45.loca.lt/track/', {
        data
    })
    .then(res => {
        console.log(res.config.data)
    })
    .catch(error => {
        console.error(error)
    })