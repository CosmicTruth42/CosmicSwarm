'use client';

import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [swarmData, setSwarmData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdate, setLastUpdate] = useState<Date | null>(null);
  const [refreshCount, setRefreshCount] = useState(0);

  const fetchData = async () => {
    try {
      console.log('Auto-Refresh ausgeführt um', new Date().toLocaleTimeString());
      setRefreshCount(prev => prev + 1);

      const response = await fetch('https://cosmicswarm-backend-v5.onrender.com/swarm', {
        cache: 'no-store',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error(`Server-Fehler: ${response.status}`);
      }

      const data = await response.json();
      setSwarmData(data);
      setLastUpdate(new Date());
      setError(null);
    } catch (err) {
      console.error('Fetch-Fehler:', err);
      setError('Verbindung zum Swarm-Server fehlgeschlagen');
      setSwarmData(null);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  const getTimeText = () => {
    if (!lastUpdate) return "wird aktualisiert...";
    const seconds = Math.round((Date.now() - lastUpdate.getTime()) / 1000);
    if (seconds < 5) return "gerade eben aktualisiert";
    if (seconds < 60) return `vor ${seconds} Sekunden`;
    if (seconds < 3600) return `vor ${Math.round(seconds / 60)} Minuten`;
    return `vor ${Math.round(seconds / 3600)} Stunden`;
  };

  const currentDate = new Date().toLocaleDateString('de-DE', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });

  const shareText = `Mein AI-Schwarm hat gerade ${swarmData?.avgFit || 90}% für evolvierende Dark Energy berechnet!\n\n"${swarmData?.consensus || ''}"\n\nLive Dashboard: https://cosmicswarm.vercel.app #CosmicTruth42 #AISwarm`;

  return (
    <div className="min-h-screen bg-black text-white p-8 font-mono">
      <div className="max-w-6xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-6xl font-extrabold mb-2 bg-gradient-to-r from-purple-500 via-cyan-400 to-purple-500 bg-clip-text text-transparent">
            CosmicTruth42
          </h1>
          <p className="text-gray-400 text-lg">
            Grok's Cosmic Swarm • Live • {currentDate}
          </p>
        </div>

        {error && <div className="bg-red-900/50 border border-red-500/50 rounded-2xl p-6 mb-8 text-center"><p className="text-red-300">{error}</p></div>}

        <div className="bg-gradient-to-br from-zinc-950 to-black border border-cyan-600/30 rounded-3xl p-10 mb-12 text-center shadow-2xl">
          <p className="text-cyan-400 text-sm uppercase tracking-widest mb-4 font-semibold">Swarm-Konsens</p>
          <p className="text-3xl md:text-4xl font-medium leading-tight mb-6">
            {swarmData?.consensus || "Lade Konsens..."}
          </p>
          <p className="text-6xl md:text-7xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-500">
            {swarmData?.avgFit || 0}%
          </p>
          <p className="text-gray-400 mt-6 text-sm">
            Zuletzt aktualisiert: {getTimeText()} (Auto-Refresh alle 30s)
          </p>
        </div>

        <div className="text-center mb-8">
          <button onClick={fetchData} className="bg-gradient-to-r from-cyan-600 to-purple-600 hover:from-cyan-700 hover:to-purple-700 text-white font-bold py-3 px-8 rounded-full transition-all">
            Manuell aktualisieren (Test)
          </button>
          <p className="text-gray-500 text-sm mt-2">Refreshs ausgeführt: {refreshCount}</p>
        </div>

        <h2 className="text-3xl text-purple-400 mb-8 font-bold text-center">Agenten-Beiträge</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {swarmData?.insights?.map((insight: string, index: number) => (
            <div key={index} className="bg-zinc-950 border border-zinc-800 rounded-2xl p-8 hover:border-cyan-500/50 transition-all duration-300 shadow-lg overflow-hidden max-h-[520px] overflow-y-auto">
              <div className="text-base text-gray-200 leading-relaxed whitespace-pre-wrap break-words">
                {insight.split('\n').map((line, i) => {
                  if (line.includes('Fit') || line.includes('Potenzial') || line.includes('Validation')) {
                    return <p key={i} className="font-bold text-cyan-300 mb-2">{line}</p>;
                  }
                  if (line.startsWith('Rat:') || line.startsWith('Spezifisch für')) {
                    return <p key={i} className="text-emerald-300 font-semibold mt-4">{line}</p>;
                  }
                  return <p key={i} className="mb-2">{line}</p>;
                })}
              </div>
            </div>
          )) || <p className="text-center text-gray-400 col-span-2">Lade Beiträge...</p>}
        </div>

        <div className="mt-12 bg-zinc-950 border border-emerald-500/30 rounded-2xl p-6 text-center">
          <p className="text-emerald-400 text-sm mb-3">On-Chain Log • CosmicTruth42</p>
          <p className="font-mono text-xs break-all text-emerald-300">
            {swarmData?.hash || "Lade Hash..."}
          </p>
        </div>

        <div className="mt-12 text-center">
          <button onClick={() => { navigator.clipboard.writeText(shareText); alert('Text kopiert – teile auf X/Moltbook!'); }} 
                  className="bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-700 hover:to-cyan-700 text-white font-bold py-4 px-12 rounded-full transition-all text-lg shadow-lg">
            Teilen auf X / Moltbook
          </button>
        </div>

        <div className="text-center text-xs text-gray-600 mt-16">
          Built with Grok • Truth first • Cosmic Swarm • Auto-Refresh alle 30s
        </div>
      </div>
    </div>
  );
}