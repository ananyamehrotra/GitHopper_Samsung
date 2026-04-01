import React, { useEffect, useRef } from 'react';
import './PlasmaBackground.css';

export function PlasmaBackground() {
    const canvasRef = useRef(null);
    const mouseRef = useRef({ x: 0, y: 0 });

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        let W, H, t = 0;

        const off = document.createElement('canvas');
        const octx = off.getContext('2d');
        const SCALE = 2;
        let oW, oH;

        function resize() {
            W = canvas.width = window.innerWidth;
            H = canvas.height = window.innerHeight;
            oW = Math.ceil(W / SCALE);
            oH = Math.ceil(H / SCALE);
            off.width = oW;
            off.height = oH;
        }

        function plasmaColor(v) {
            // Only green plasma - no rainbow colors
            const intensity = v;
            return [
                0,
                Math.floor(intensity * 255),
                0
            ];
        }

        function handleMouseMove(e) {
            mouseRef.current.x = e.clientX / W;
            mouseRef.current.y = e.clientY / H;
        }

        function render() {
            t += 0.025;
            const imageData = octx.createImageData(oW, oH);
            const data = imageData.data;

            const mx = mouseRef.current.x;
            const my = mouseRef.current.y;

            for (let y = 0; y < oH; y++) {
                for (let x = 0; x < oW; x++) {
                    const nx = x / oW;
                    const ny = y / oH;

                    // Multiple flowing layers for liquid effect
                    const v1 = Math.sin(nx * 10 + t * 0.5) * Math.cos(ny * 5 - t * 0.3);
                    const v2 = Math.sin(ny * 8 - t * 0.4) * Math.cos(nx * 6 + t * 0.2);
                    const v3 = Math.sin((nx + ny) * 7 + t * 0.6);

                    // Perlin-like turbulence
                    const v4 = Math.sin(Math.sqrt(
                        (nx - 0.5 + Math.sin(t * 0.3) * 0.3) ** 2 +
                        (ny - 0.5 + Math.cos(t * 0.25) * 0.3) ** 2
                    ) * 18 - t * 0.8);

                    // High frequency detail
                    const v5 = Math.sin(
                        nx * 15 * Math.cos(t * 0.4) +
                        ny * 12 * Math.sin(t * 0.35) +
                        t * 0.7
                    );

                    // Mouse reactivity
                    const dx = nx - mx;
                    const dy = ny - my;
                    const distToMouse = Math.sqrt(dx * dx + dy * dy);
                    const mouseInfluence = Math.sin(distToMouse * 8 - t * 1.5) * Math.exp(-distToMouse * 3);

                    // Combine all layers
                    const combined = (v1 + v2 + v3 + v4 + v5 + mouseInfluence * 2) / 6;
                    const norm = (combined + 1) / 2;
                    const [r, g, b] = plasmaColor(norm);

                    const i = (y * oW + x) * 4;
                    data[i] = r;
                    data[i + 1] = g;
                    data[i + 2] = b;
                    data[i + 3] = 255;
                }
            }

            octx.putImageData(imageData, 0, 0);
            ctx.clearRect(0, 0, W, H);
            ctx.imageSmoothingEnabled = true;
            ctx.drawImage(off, 0, 0, W, H);
            requestAnimationFrame(render);
        }

        window.addEventListener('resize', resize);
        window.addEventListener('mousemove', handleMouseMove);
        resize();
        render();

        return () => {
            window.removeEventListener('resize', resize);
            window.removeEventListener('mousemove', handleMouseMove);
        };
    }, []);

    return <canvas ref={canvasRef} id="plasma" className="plasma-canvas" />;
}
