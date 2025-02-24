output "ingress_node_ip" {
  value = aws_instance.ingress_node.public_ip
}

output "control_plane_node_ip" {
  value = aws_instance.control_plane_node.public_ip
}

output "worker_node_1_public_ip" {
  value = aws_instance.worker_node_1.public_ip
}

output "worker_node_2_public_ip" {
  value = aws_instance.worker_node_2.public_ip
}

output "worker_node_3_public_ip" {
  value = aws_instance.worker_node_3.public_ip
}

output "ingress_node_id" {
  value = aws_instance.ingress_node.id
}

output "control_plane_node_id" {
  value = aws_instance.control_plane_node.id
}

output "worker_node_1_public_id" {
  value = aws_instance.worker_node_1.id
}

output "worker_node_2_public_id" {
  value = aws_instance.worker_node_2.id
}

output "worker_node_3_public_id" {
  value = aws_instance.worker_node_3.id
}
