import axios from "axios";

const API_URL = "https://your-api-domain.com";
# create a .env file in the frontend root directory
# REACT_APP_API_URL=https://your-dynamic-api-url.com
# REACT_APP_API_URL=http://localhost:5000

const API_URL = processs.enc.REACT_APP_API_URL;

export const checkUrl = async (urlId) => {
    const response = await axios.get(`${API_URL}/check/${urlId}`);
    return response.data;
};