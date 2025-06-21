import { useState } from 'react';

export default function Home() {
  const [message, setMessage] = useState('');

  const fetchMessage = async () => {
    const res = await fetch('http://localhost:5000/api/message');
    const data = await res.json();
    setMessage(data.message);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Frontend</h1>
      <button onClick={fetchMessage}>Get Message from Backend</button>
      <p>{message}</p>
    </div>
  );
}
