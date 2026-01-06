from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt


load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")  # or other Groq models

st.header('Reasearch Tool')

paper_input = st.selectbox(
    "Select Research Paper Name",
 [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
    "Vision Transformer ViT",
    "CLIP: Connecting Text and Images",
    "PaLM: Scaling Language Modeling",
    "LoRA: Low Rank Adaptation of Large Language Models",
    "DINO: Self-Supervised Vision Learning",
    "UNet: Convolutional Networks for Biomedical Image Segmentation",
    "ResNet: Deep Residual Learning",
    "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context",
    "RoBERTa: A Robustly Optimized BERT Pretraining Approach",
    "ALBERT: A Lite BERT for Self-supervised Learning",
    "T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer",
    "XLNet: Generalized Autoregressive Pretraining",
    "ELECTRA: Pre-training Text Encoders as Discriminators",
    "GPT-2: Better Language Models and Their Implications",
    "LLaMA: Open and Efficient Foundation Language Models",
    "Mamba State Space Models",
    "SAM: Segment Anything Model",
    "Stable Diffusion: High Resolution Text-to-Image Synthesis",
    "DDPM: Denoising Diffusion Probabilistic Models",
    "DDIM: Denoising Diffusion Implicit Models",
    "NeRF: Representing Scenes as Neural Radiance Fields",
    "StyleGAN2: Image Generation Architecture",
    "StyleGAN: A Style-Based Generator Architecture for GANs",
    "CycleGAN: Unpaired Image-to-Image Translation",
    "Pix2Pix: Image-to-Image Translation with Conditional GANs",
    "Mask R-CNN",
    "Faster R-CNN",
    "YOLOv1: You Only Look Once",
    "YOLOv3: An Incremental Improvement",
    "YOLOv5 Research Overview",
    "Swin Transformer: Hierarchical Vision Transformer",
    "DETR: End-to-End Object Detection with Transformers",
    "MobileNetV2: Inverted Residuals and Linear Bottlenecks",
    "EfficientNet: Rethinking Model Scaling",
    "AlexNet: ImageNet Classification",
    "VGG16: Deep Convolutional Networks",
    "Inception v3",
    "ReLU: Rectified Linear Units",
    "Batch Normalization: Accelerating Neural Networks",
    "Layer Normalization",
    "RMSNorm",
    "GloVe: Global Vectors for Word Representation",
    "Word2Vec: Distributed Representations of Words",
    "Seq2Seq Learning",
    "Pointer Networks",
    "Graph Attention Networks (GAT)",
    "Graph Convolutional Networks (GCN)",
    "Neural ODEs",
    "LSTM: Long Short Term Memory",
    "GRU: Gated Recurrent Units",
    "Variational Autoencoders (VAE)",
    "Beta-VAE",
    "GAN: Generative Adversarial Networks",
    "WGAN: Wasserstein GAN",
    "WGAN-GP: Gradient Penalty",
    "BigGAN",
    "SAM Optimizer: Sharpness Aware Minimization",
    "Adam Optimizer",
    "Adagrad",
    "RMSProp",
    "Dropout: Preventing Overfitting",
    "Neural Architecture Search (NAS)",
    "AlphaGo Zero",
    "AlphaFold: Protein Structure Prediction",
    "Deep Q-Learning",
    "Proximal Policy Optimization (PPO)",
    "Soft Actor Critic (SAC)",
    "A3C: Asynchronous Advantage Actor Critic",
    "Deep Deterministic Policy Gradient (DDPG)",
    "Meta Learning: MAML",
    "SimCLR: Contrastive Learning",
    "MoCo: Momentum Contrast",
    "BYOL: Bootstrap Your Own Latent",
    "Barlow Twins",
    "Self-Supervised Learning: Survey",
    "Few-Shot Learning with Prototypical Networks",
    "Siamese Networks for One-Shot Learning",
    "Contrastive Predictive Coding (CPC)",
    "Reinforcement Learning: Sutton & Barto Paper",
    "Mixture of Experts: GShard",
    "Switch Transformer",
    "FlashAttention: Fast Transformer Attention",
    "Phi-2: Small Language Models with Big Capabilities",
    "GPT-4 Technical Report",
    "DALL·E: Zero-Shot Text-to-Image Generation",
    "DALL·E 2: Hierarchical Diffusion for Images",
    "Imagen: Photorealistic Text-to-Image Diffusion Models",
    "ControlNet: Conditioning Diffusion Models",
    "DreamFusion: Text-to-3D",
    "SAM2: Next Generation Segment Anything",
    "Whisper: Speech Recognition",
    "WaveNet: Audio Generation",
    "Tacotron2: Text to Speech Synthesis",
    "DeepSpeech",
    "SpecAugment",
    "Hybrid CNN Transformer Architectures"
]

)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical",
        "Visual Analogy Based",
        "Real World Examples",
        "Step by Step Breakdown",
        "Use Case Focused",
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1 to 2 paragraphs)",
        "Medium (3 to 5 paragraphs)",
        "Long (detailed explanation)",
        "Bullet Points Only",
        "Extended Deep Dive",
    ]
)

# Load the prompt template from the json file
prompt_template = load_prompt("04_Prompts_in_LangChain/Efficient_prompt.json")

if st.button('Generate Explanation'):
    chain = prompt_template | model 
    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })

    st.subheader('Generated Explanation:')
    st.write(response.content)
   