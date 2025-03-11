import React, { useState } from "react";
import axios from "axios";

const API_URL = "https://your-api-domain.com";

function AdminDashboard() {
    const [urlMappings, setUrlMappings] = useState([]);

    const fetchUrls = async () => {
        const response = await axios.get(`${API_URL}/admin/get-urls`);
        setUrlMappings(response.data);
    };

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <button onClick={fetchUrls}>Load URLs</button>
            <ul>
                {urlMappings.map((url) => (
                    <li key={url.id}>
                        ID: {url.id}, Safe URL: {url.safe_url}, Real URL: {url.real_url}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default AdminDashboard;