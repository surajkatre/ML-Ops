import pandas as pd

# Create a dictionary with the required data
data = {
    "Category": ["Speech-to-Text", "Speech-to-Text", "Speech-to-Text", "Speech-to-Text", 
                 "Text-to-Speech", "Text-to-Speech", "Text-to-Speech", "Text-to-Speech",
                 "Speaker Diarization", "Speaker Diarization", "Speaker Diarization", "Speaker Diarization",
                 "Spoken Language Model", "Spoken Language Model", "Spoken Language Model", "Spoken Language Model"],
    
    "Solution Type": ["Open-Source", "Open-Source", "Closed-Source", "Closed-Source", 
                      "Open-Source", "Open-Source", "Closed-Source", "Closed-Source",
                      "Open-Source", "Open-Source", "Closed-Source", "Closed-Source",
                      "Open-Source", "Open-Source", "Closed-Source", "Closed-Source"],
    
    "Model Name": ["Mozilla DeepSpeech", "Wav2Vec 2.0", "Google Cloud Speech-to-Text", "Microsoft Azure Speech Services",
                   "Coqui TTS", "Tacotron 2", "Amazon Polly", "Microsoft Azure TTS",
                   "pyAudioAnalysis", "Kaldi", "Google Cloud Speaker Diarization", "Otter.ai",
                   "BioBERT", "ClinicalBERT", "Nuance Dragon Medical", "Google Cloud Healthcare API"],
    
    "Description": ["Deep learning-based STT engine for transcription.",
                    "Self-supervised STT model supporting multiple languages.",
                    "Real-time, accurate speech recognition with medical applications.",
                    "Customizable speech recognition service for multilingual settings.",
                    "Highly customizable TTS engine with multilingual support.",
                    "Google's natural-sounding TTS model.",
                    "Lifelike text-to-speech capabilities with medical terminology support.",
                    "Natural-sounding voices, ideal for healthcare environments.",
                    "Python library for audio feature extraction and classification.",
                    "Speech recognition toolkit with a robust speaker diarization component.",
                    "Real-time speaker diarization for medical applications.",
                    "Diarization service for distinguishing speakers in meetings and conversations.",
                    "Language model fine-tuned for biomedical literature.",
                    "Designed for clinical conversations and healthcare applications.",
                    "Dictation software with medical-specific language models.",
                    "API for integrating with medical records systems and understanding conversations."],
    
    "Link": ["https://github.com/mozilla/DeepSpeech", "https://huggingface.co/models?sort=downloads&search=wav2vec2", 
             "https://cloud.google.com/speech-to-text", "https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/",
             "https://github.com/coqui-ai/TTS", "https://github.com/Rayhane-mamah/Tacotron-2",
             "https://aws.amazon.com/polly/", "https://azure.microsoft.com/en-us/services/cognitive-services/text-to-speech/",
             "https://github.com/tyiannak/pyAudioAnalysis", "https://github.com/kaldi-asr/kaldi",
             "https://cloud.google.com/speech-to-text/docs/multiple-voices", "https://otter.ai/",
             "https://github.com/dmis-lab/biobert", "https://github.com/EmilyAlsentzer/clinicalBERT",
             "https://www.nuance.com/healthcare.html", "https://cloud.google.com/solutions/healthcare"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_path = "doctor_patient_communication_system.xlsx"
df.to_excel(file_path, index=False)

