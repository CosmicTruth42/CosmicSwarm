export default async function handler(req, res) {
  try {
    // Hier rufen wir deinen lokalen Python-Server auf – aber wir wechseln später zu einer echten Serverless-Alternative
    const response = await fetch('http://127.0.0.1:8000/swarm', {
      cache: 'no-store',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    if (!response.ok) {
      throw new Error(`Backend-Fehler: ${response.status}`);
    }

    const data = await response.json();
    res.status(200).json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: 'Verbindung zum Backend fehlgeschlagen' });
  }
};