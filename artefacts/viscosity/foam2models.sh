#!/usr/bin/env bash
set -e

foam=${1}

dir=$(cd `dirname $0` && pwd)
source ${dir}/env.sh

models_dir="${foam}/src/transportModels"
target_model='viscosityModel'
target_file=${viscosity_file}

artefacts/foam2models.sh ${models_dir} ${target_model} ${target_file}
