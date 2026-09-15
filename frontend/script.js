// This placeholder will be updated with your API Gateway endpoint
const API_URL = "https://sc1qo7sau6.execute-api.us-east-1.amazonaws.com/visitors";

async function fetchVisitorCount() {
  try {
    const res = await fetch(API_URL);
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
    const data = await res.json();
    document.getElementById("visitor-count").innerText = data.count;
  } catch (err) {
    console.error("Counter load error:", err);
    document.getElementById("visitor-count").innerText = "1";
  }
}

document.addEventListener("DOMContentLoaded", fetchVisitorCount);