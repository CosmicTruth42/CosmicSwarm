import { NextResponse } from 'next/server';

export async function GET() {
  const urls = ['http://127.0.0.1:8000/swarm', 'http://localhost:8000/swarm'];

  for (const url of urls) {
    try {
      console.log('Versuche Fetch von:', url);
      const response = await fetch(url, {
        cache: 'no-store',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      console.log('Response Status von', url, ':', response.status);

      if (response.ok) {
        const data = await response.json();
        console.log('Erfolg von', url);
        return NextResponse.json(data);
      }
    } catch (error) {
      console.error('Fetch-Fehler von', url, ':', error);
    }
  }

  console.error('Alle Fetch-Versuche fehlgeschlagen');
  return NextResponse.json({
    topic: "Verbindung fehlgeschlagen",
    insights: ["Kein Zugriff auf Backend – bitte Python-Server prüfen"],
    consensus: "Fehler",
    avgFit: 0,
    hash: "Fehler"
  });
}