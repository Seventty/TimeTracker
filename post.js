const axios = require('axios');
const data = require('./endpoint.json');
 
axios
    .post('https://chatty-dingo-57.loca.lt/track/', {
        data
    })
    .catch(error => {
        console.error(error)
    })