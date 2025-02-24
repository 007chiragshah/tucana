#!/usr/bin/env bash

{
  echo "INGRESS_NODE_IP=$(terraform -chdir=infra/dev output -raw ingress_node_ip)"
  echo "CONTROL_PLANE_NODE_IP=$(terraform -chdir=infra/dev output -raw control_plane_node_ip)"
  echo "WORKER_NODE_1_PUBLIC_IP=$(terraform -chdir=infra/dev output -raw worker_node_1_public_ip)"
  echo "WORKER_NODE_2_PUBLIC_IP=$(terraform -chdir=infra/dev output -raw worker_node_2_public_ip)"
  echo "WORKER_NODE_3_PUBLIC_IP=$(terraform -chdir=infra/dev output -raw worker_node_3_public_ip)"
} > .env