import os
from synthetic.generate_audio import AudioGenerator
from pathlib import Path

def main():
    # Initialize the audio generator
    generator = AudioGenerator()
    
    # Set up the transcript path
    transcript_path = Path('data/synthetic/text/prenatal_exam.txt')
    
    print(f"\nGenerating audio for: {transcript_path}")
    print("-" * 50)
    
    # Generate the audio
    audio_path = generator.create_conversation_audio(transcript_path)
    
    if audio_path:
        print(f"\nSuccessfully generated audio: {audio_path}")
        
        # Now process the audio through the analysis pipeline
        from continuous_analysis.transcribe_analyze import AudioAnalyzer
        
        print("\nProcessing audio through analysis pipeline...")
        analyzer = AudioAnalyzer()
        result = analyzer.process_audio_file(audio_path)
        
        if result:
            print("\nProcessing complete. Files generated:")
            for key, value in result.items():
                print(f"{key}: {value}")
    else:
        print("\nFailed to generate audio")

if __name__ == "__main__":
    main() 