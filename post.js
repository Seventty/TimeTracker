const axios = require('axios');
const data = require('./endpoint.json');
 
axios
    .post('example.com/track/', {
        data
    })
    .catch(error => {
        console.error(error)
    })
