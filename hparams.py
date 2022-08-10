import tensorflow as tf
from text import symbols


class create_hparams:  
    """Create model hyperparameters. Parse nondefault from given string."""
    def __init__(self,hparams_string=None, verbose=False):
        
    
        ################################
        # Experiment Parameters        #
        ################################
        self.epochs=100
        self.iters_per_checkpoint=500
        self.seed=1234
        self.dynamic_loss_scaling=True
        self.fp16_run=False
        self.distributed_run=False
        self.dist_backend="nccl"
        self.dist_url="tcp://localhost:54321"
        self.cudnn_enabled=True
        self.cudnn_benchmark=False
        self.ignore_layers=['embedding.weight']

        ################################
        # Data Parameters             #
        ################################
        self.load_mel_from_disk=False
        self.training_files='filelists/transcript_train.txt'
        self.validation_files='filelists/transcript_val.txt'
        self.text_cleaners=['japanese_cleaners']

        ################################
        # Audio Parameters             #
        ################################
        self.max_wav_value=32768.0
        self.sampling_rate=22050
        self.filter_length=1024
        self.hop_length=256
        self.win_length=1024
        self.n_mel_channels=80
        self.mel_fmin=0.0
        self.mel_fmax=8000.0

        ################################
        # Model Parameters             #
        ################################
        self.n_symbols=len(symbols)
        self.symbols_embedding_dim=512

        # Encoder parameters
        self.encoder_kernel_size=5
        self.encoder_n_convolutions=3
        self.encoder_embedding_dim=512

        # Decoder parameters
        self.n_frames_per_step=1  # currently only 1 is supported
        self.decoder_rnn_dim=1024
        self.prenet_dim=256
        self.max_decoder_steps=1000
        self.gate_threshold=0.5
        self.p_attention_dropout=0.1
        self.p_decoder_dropout=0.1

        # Attention parameters
        self.attention_rnn_dim=1024
        self.attention_dim=128

        # Location Layer parameters
        self.attention_location_n_filters=32
        self.attention_location_kernel_size=31

        # Mel-post processing network parameters
        self.postnet_embedding_dim=512
        self.postnet_kernel_size=5
        self.postnet_n_convolutions=5

        ################################
        # Optimization Hyperparameters #
        ################################
        self.use_saved_learning_rate=False
        self.learning_rate=1e-3
        self.weight_decay=1e-6
        self.grad_clip_thresh=1.0
        self.batch_size=64
        self.mask_padding=True  # set model's padded outputs to padded values
    

        if hparams_string:
        #    tf.logging.info('Parsing command line hparams: %s', hparams_string)
        #    hparams.parse(hparams_string)
            pass

        if verbose:
        #    tf.logging.info('Final parsed hparams: %s', hparams.values())
            pass
