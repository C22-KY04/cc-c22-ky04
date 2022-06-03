function error_responses(status_code) {
    let json_code = {};
    if(status_code == 400) {
        return json_code = {
            status: 'Bad Request',
            message: error.message,
        };
    } else if(status_code == 404) {
        return json_code = {
            status: 'Not Found',
            message: 'The item/record not found.',
        };
    }
}

module.exports = { error_responses };
