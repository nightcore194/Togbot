import os
from flask import request, Blueprint
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from aiortc import RTCPeerConnection, RTCSessionDescription
import asyncio
import uuid

voice_view = Blueprint('voice', __name__, url_prefix='/voice')
connections = {}


@voice_view.route('/offer', methods=['POST'])
async def offer():
    data = request.json
    offer = RTCSessionDescription(sdp=data['sdp'], type=data['type'])
    pc = RTCPeerConnection()
    connections[uuid.uuid4()] = pc

    @pc.on('icecandidate')
    async def on_icecandidate(candidate):
        await pc.addIceCandidate(candidate)

    await pc.setRemoteDescription(offer)

    # Create answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return {
        'sdp': pc.localDescription.sdp,
        'type': pc.localDescription.type
    }
