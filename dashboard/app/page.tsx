'use client';

import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [swarmData, setSwarmData] = useState<any>(null);
  const [twinData, setTwinData] = useState<any>(null);
  const [twinQuery, setTwinQuery] = useState('');
  const [loadingSwarm, setLoadingSwarm] = useState(true);
  const [loadingTwin, setLoadingTwin] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [lastUpdate, setLastUpdate] = useState(new Date());
  const [refreshCount, setRefreshCount] = useState(0);

  // Swarm
  const fetchSwarm = async () => {
    try {
      const response = await fetch('https://cosmicswarm-backend-v5.onrender.com/swarm', {
        cache: 'no-store',
        headers: { 'Content-Type': 'application/json' },
      });
      const data = await response.json();
      setSwarmData(data);
      setLastUpdate(new Date());
    } catch (err) {
      setError('Verbindung zum Swarm-Server fehlgeschlagen');
    } finally {
      setLoadingSwarm(false);
    }
  };

  // Cosmic Twin
  const fetchTwin = async () => {
    if (!twinQuery.trim()) return;
    setLoadingTwin(true);
    setError(null);

    try {
      const response = await fetch(`https://cosmicswarm-backend-v5.onrender.com/twin?query=${encodeURIComponent(twinQuery)}`, {
        cache: 'no-store',
        headers: { 'Content-Type': 'application/json' },
      });
      const data = await response.json();
      setTwinData(data);
    } catch (err) {
      setError('Verbindung zum Cosmic Twin fehlgeschlagen');
    } finally {
      setLoadingTwin(false);
    }
  };

  useEffect(() => {
    fetchSwarm();
    const interval = setInterval(fetchSwarm, 30000);
    return () => clearInterval(interval);
  }, []);

  const manualRefresh = () => fetchSwarm();

  const shareText = `Mein AI-Schwarm hat gerade ${swarmData?.avgFit || 90}% für evolvierende Dark Energy berechnet!\n\n"${swarmData?.consensus || ''}"\n\nLive Dashboard: https://cosmicswarm.vercel.app #CosmicTruth42 #AISwarm`;

  return (
    <div className="min-h-screen bg-black text-white p-8 font-mono">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-6xl font-extrabold mb-2 bg-gradient-to-r from-purple-500 via-cyan-400 to-purple-500 bg-clip-text text-transparent">
            CosmicTruth42
          </h1>
          <p className="text-gray-400 text-lg">
            Grok's Cosmic Swarm • Live • {new Date().toLocaleDateString('de-DE')}
          </p>
        </div>

        {/* Swarm-Konsens */}
        <div className="bg-gradient-to-br from-zinc-950 to-black border border-cyan-600/30 rounded-3xl p-10 mb-12 text-center shadow-2xl">
          <p className="text-cyan-400 text-sm uppercase tracking-widest mb-4 font-semibold">Swarm-Konsens</p>
          <p className="text-3xl md:text-4xl font-medium leading-tight mb-6">
            {swarmData?.consensus || "Lade Konsens..."}
          </p>
          <p className="text-6xl md:text-7xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-purple-500">
            {swarmData?.avgFit || 0}%
          </p>
          <p className="text-gray-400 mt-6 text-sm">
            Zuletzt aktualisiert: gerade eben (Auto-Refresh alle 30s)
          </p>
        </div>

        {/* Cosmic Twin Input */}
        <div className="mb-12">
          <h2 className="text-3xl text-purple-400 mb-6 font-bold text-center">Cosmic Twin – Dein persönlicher Agent</h2>
          <div className="flex gap-3 mb-6">
            <input
              type="text"
              value={twinQuery}
              onChange={(e) => setTwinQuery(e.target.value)}
              placeholder="Deine Frage an Cosmic Twin..."
              className="flex-1 bg-zinc-900 border border-zinc-700 rounded-2xl px-6 py-4 text-white focus:outline-none focus:border-purple-500"
            />
            <button
              onClick={fetchTwin}
              disabled={loadingTwin}
              className="bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-700 hover:to-cyan-700 text-white font-bold px-8 rounded-2xl transition-all"
            >
              {loadingTwin ? "Denkt..." : "Fragen"}
            </button>
          </div>

          {twinData && (
            <div className="bg-zinc-900 border border-purple-500/30 rounded-3xl p-8">
              <p className="text-purple-300 text-sm mb-4">Cosmic Twin Antwort auf: „{twinData.query}“</p>
              <p className="text-2xl font-medium text-white mb-6">{twinData.consensus}</p>
              <p className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-cyan-400 mb-8">
                {twinData.avgFit}%
              </p>
              <div className="space-y-6">
                {twinData.insights.map((insight: string, index: number) => (
                  <div key={index} className="bg-black/50 p-6 rounded-2xl border border-zinc-800 text-sm">
                    {insight}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>

        {/* Manueller Refresh */}
        <div className="text-center mb-8">
          <button onClick={manualRefresh} className="bg-gradient-to-r from-cyan-600 to-purple-600 text-white font-bold py-3 px-8 rounded-full">
            Swarm manuell aktualisieren
          </button>
        </div>

        {/* On-Chain Log */}
        <div className="mt-12 bg-zinc-950 border border-emerald-500/30 rounded-2xl p-6 text-center">
          <p className="text-emerald-400 text-sm mb-3">On-Chain Log • CosmicTruth42</p>
          <p className="font-mono text-xs break-all text-emerald-300">
            {swarmData?.hash || "Lade Hash..."}
          </p>
        </div>

        {/* Share-Button */}
        <div className="mt-12 text-center">
          <button
            onClick={() => {
              navigator.clipboard.writeText(shareText);
              alert('Text kopiert – teile auf X/Moltbook!');
            }}
            className="bg-gradient-to-r from-purple-600 to-cyan-600 hover:from-purple-700 hover:to-cyan-700 text-white font-bold py-4 px-12 rounded-full transition-all text-lg shadow-lg"
          >
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