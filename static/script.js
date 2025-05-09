async function getRecommendations() {
  const mood = document.getElementById("mood").value;
  const res = await fetch("/get_recommendations", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mood })
  });
  const text = await res.text();
  document.getElementById("result").innerText = text;
}
