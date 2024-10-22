# ATDL Assignment 2
Paper: _Diffusion Models Beat GANs on Image Synthesis_

## Objective
Replicate a subset of the experiments presented in the paper, including:
* Train diffusion models on LSUN Bedrooms & ImageNet 64 datasets without classifier guidance
* Evaluate the trained models on the corresponding reference batches
* Evaluate the BigGAN-deep model trained on ImageNet 64 on the same reference batches
* Compare and discuss the evaluation results

## Scripts we added
`model.py` and `model_lsun.py`: for printing the architecture and number of parameters of the models
`sample.ipynb`: for showing the sample images generated through our trained models

## Diffusion on windows

The following is a guide for some of the extra steps taken to get the training working on windows 11 with rtx 4060 nvidia gpu

git clone https://github.com/openai/guided-diffusion

git clone https://github.com/fyu/lsun


### Disable libuv on Windows:

$env:USE_LIBUV="0"

python scripts/image_train.py --data_dir datasets/lsun_train_output_dir --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16 --diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False --use_scale_shift_norm False --lr 2e-5 --batch_size 32 --microbatch 1 --save_interval 500

### sampling

python scripts/image_sample.py --model_path .\models\openai-2024-10-22-04-44-36-915977\ema_0.9999_002000.pt --image_size 256 --num_channels 128 --num_res_blocks 2 --num_heads 1 --learn_sigma True --use_scale_shift_norm False --attention_resolutions 16 --diffusion_steps 1000 --noise_schedule linear --rescale_learned_sigmas False --rescale_timesteps False --use_scale_shift_norm False --num_samples 100 --batch_size 1

### Evaluation

python .\evaluations\evaluator.py .\models\pretrained\VIRTUAL_lsun_bedroom256.npz .\models\openai-2024-10-22-16-37-25-946078\samples_100x256x256x3.npz

