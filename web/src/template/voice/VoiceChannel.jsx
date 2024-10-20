import React,{ useEffect, useRef, useState } from 'react';

export default function VoiceChannel() {
    const audioRef = useRef(null);
    const [pc, setPc] = useState(null);

    const startCall = async () => {
        const newPc = new RTCPeerConnection();
        setPc(newPc);

        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        stream.getTracks().forEach(track => newPc.addTrack(track, stream));

        newPc.ontrack = event => {
            const audioStream = event.streams[0];
            if (audioRef.current) {
                audioRef.current.srcObject = audioStream;
            }
        };

        const offer = await newPc.createOffer();
        await newPc.setLocalDescription(offer);

        const response = await fetch('/offer', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ sdp: offer.sdp, type: offer.type })
        });

        const answer = await response.json();
        await newPc.setRemoteDescription(new RTCSessionDescription(answer));
    };

    const logout = async () => {
        await fetch('/logout', { method: 'POST' });
        // Handle logout UI change if needed
    };

    return (
        <div>
            <h1>Voice Channel</h1>
            <button onClick={startCall}>Start Call</button>
            <button onClick={logout}>Logout</button>
            <audio ref={audioRef} autoPlay></audio>
        </div>
    );
}

