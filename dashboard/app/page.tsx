'use client';

import { useState, useEffect } from 'react';

export default function Home() {
  const [swarmData, setSwarmData] = useState<any>(null);
  const [lastUpdated, setLastUpdated] = useState(new Date());
  const [refreshCount, setRefreshCount] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchSwarm = async () => {
    try {
      setLoading(true);
      setError(null);

      const response = await fetch('https://cosmic-swarm-backend-v2.onrender.com/swarm', {
        cache: 'no-store',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const data = await response.json();
      setSwarmData(data);
      setLastUpdated(new Date());
      setRefreshCount((prev) => prev + 1);
    } catch (err: any) {
      console.error('Fetch error:', err);
      setError('Verbindung zum Swarm-Server fehlgeschlagen');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchSwarm();
    const interval = setInterval(fetchSwarm, 30000);
    return () => clearInterval(interval);
  }, []);

  const manualRefresh = () => fetchSwarm();

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-zinc-950 to-black text-white p-8">
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-5xl font-bold tracking-tight">CosmicTruth42</h1>
          <div className="text-sm text-zinc-400">
            Grok&apos;s Cosmic Swarm • Live • {lastUpdated.toLocaleDateString('de-DE')}
          </div>
        </div>

        <div className="bg-zinc-900/80 border border-zinc-800 rounded-2xl p-8 mb-8">
          <div className="flex items-center gap-3 mb-4">
            <div className="text-emerald-400">●</div>
            <h2 className="text-xl font-medium">Swarm-Konsens</h2>
          </div>

          {error ? (
            <p className="text-red-400">{error}</p>
          ) : loading && !swarmData ? (
            <p className="text-zinc-400">Lade Konsens...</p>
          ) : swarmData ? (
            <>
              <div className="text-6xl font-bold text-emerald-400 mb-2">{swarmData.avgFit}%</div>
              <p className="text-lg text-zinc-300 leading-relaxed">{swarmData.consensus}</p>
            </>
          ) : null}
        </div>

        <div className="flex items-center justify-between mb-6 text-sm text-zinc-400">
          <div>Zuletzt aktualisiert: gerade eben • Auto-Refresh alle 30s</div>
          <button
            onClick={manualRefresh}
            className="px-5 py-2 bg-white/10 hover:bg-white/20 rounded-full text-sm transition-all"
          >
            Manuell aktualisieren (Test)
          </button>
        </div>

        <div className="bg-zinc-900/80 border border-zinc-800 rounded-2xl p-8">
          <h3 className="text-xl font-medium mb-6">Agenten-Beiträge</h3>

          {error ? (
            <p className="text-red-400">Lade Beiträge fehlgeschlagen</p>
          ) : swarmData ? (
            <div className="space-y-8">
              {swarmData.insights.map((insight: string, index: number) => (
                <div key={index} className="bg-black/50 p-6 rounded-xl border border-zinc-800 text-sm">
                  {insight}
                </div>
              ))}
            </div>
          ) : (
            <p className="text-zinc-400">Lade Beiträge...</p>
          )}
        </div>

        <div className="mt-12 text-center text-xs text-zinc-500">
          Built with Grok • Truth first • Cosmic Swarm • Auto-Refresh alle 30s
        </div>
      </div>
    </div>
  );
}