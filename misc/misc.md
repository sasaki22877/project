apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

export PATH=~/anaconda3/bin:$PATH
conda config --set auto_activate_base false




conda create --name tg_bot -c conda-forge python=3.11

conda activate tg_bot