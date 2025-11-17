'use client';

export default function Home() {
  async function pingApi() {
    const res = await fetch("https://deployment1-backend.onrender.com/ping");
    const data = await res.json();
    alert(data.message);
  }

  return (
    <main style={{ padding: 40 }}>
      <h1>Next.js → FastAPI Test</h1>
      <button
        onClick={pingApi}
        style={{
          padding: "10px 20px",
          background: "black",
          color: "white",
          borderRadius: "8px",
        }}
      >
        Ping API
      </button>
    </main>
  );
}
