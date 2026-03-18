'use client';

import { useEffect } from 'react';

export default function Home() {
  useEffect(() => {
    const testFetch = async () => {
      console.log('Starte Fetch...');
      try {
        const response = await fetch('https://cosmic-swarm-backend-v2.onrender.com/swarm', {
          cache: 'no-store',
          headers: { 'Content-Type': 'application/json' },
        });

        console.log('Status:', response.status);
        console.log('Response OK:', response.ok);

        const text = await response.text();
        console.log('Erste 200 Zeichen:', text.substring(0, 200));

        const data = JSON.parse(text);
        console.log('JSON erfolgreich:', data);
      } catch (err) {
        console.error('Fehler:', err);
      }
    };

    testFetch();
  }, []);

  return <div>Debug-Modus – schau in die Console (F12)</div>;
}