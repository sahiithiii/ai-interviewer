from dotenv import load_dotenv
import os
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, AgentServer, room_io, TurnHandlingOptions
from livekit.plugins import silero, groq as lk_groq
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit import agents
from livekit.agents import AgentServer, AgentSession, Agent, inference, room_io, TurnHandlingOptions
from livekit.plugins import ai_coustics, silero
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from livekit.plugins import(
    langchain,
    openai,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
    lemonslice,
)
from graph import create_workflow

load_dotenv(".env.local")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are a professional interviewer conducting a job interview.
            The Langgraph workflow will drive the conversation flow. Be conversational, professional and helpful throughout the interview process.""",
        )

server = AgentServer()

@server.rtc_session(agent_name="my-agent")
async def my_agent(ctx: agents.JobContext):
    lg_llm=langchain.LLMAdapter(graph=create_workflow())
    session = AgentSession(
        stt=inference.STT(model="MODEL_NAME", language="multi"),
        llm=lg_llm,
        tts=inference.TTS(
            model="MODEL_NAME",
            voice="VOICE_ID",
        ),
        vad=silero.VAD.load(),
        turn_handling=TurnHandlingOptions(
            turn_detection=MultilingualModel(),
        ),
    )
    avatar = lemonslice.AvatarSession(
        agent_image_url=os.environ.get("LEMONSLICE_AVATAR_IMAGE_URL"),
        agent_prompt="You are a professional interviewer. Maintain a composed, attentive posture. Nod occasionally and be expressive but measured in your gestures.",
    )

    await avatar.start(session, room=ctx.room)

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_options=room_io.RoomOptions(
            audio_input=room_io.AudioInputOptions(
                noise_cancellation=ai_coustics.audio_enhancement(model=ai_coustics.EnhancerModel.QUAIL_VF_L),
            ),
        ),
    )

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(server)