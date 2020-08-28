# First time creation

1. `pip install webviz-config`

That will ensure that user can run webviz CLI (command line interface) commands

2. `git@github.com:ingeknudsen/webviz-subsurface-on-radix.git`

Cloning the repo down to your folder

3. `git clone --depth 1 https://github.com/equinor/webviz-subsurface-testdata`

Cloning the example repo into your folder

4. `cd webviz-subsurface-on-radix`

Navigate to the repo

5. `rm -rf out && webviz build ../webviz-subsurface-testdata/webviz_examples/webviz-full-demo.yml --theme equinor --portable ./out`

Generate portable app

6. `mv ./out/assets/ ./assets`
7. `cp ./out/.dockerignore ./.dockerignore`
8. `cp ./out/theme_settings.json ./theme_settings.json`

Copy generated assets out

9.  `cp ./hack/Dockerfile ./Dockerfile`

Copy the modified dockerfile to allow it to run on Radix

9.  `cp ./hack/radixconfig.yaml ./radixconfig.yaml`

Copy the radixconfig to allow it to run on Radix. Custom config which differs from project to project is
