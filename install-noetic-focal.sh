#!/bin/bash

# Exit IF a command fail

set -e

# Intro
echo "Game's ROS Noetic Installer"
echo "============================================="
echo "This is a script to quickly install ROS Noetic."
echo "The commands that will be run is from the ROS Noetic installation guide for Ubuntu Focal. It may not work with older or newer version. Support for Focal ends in April 2025."
echo "This script should be RUN AS ROOT."
echo "(Copyright) Thapat A. GPLv3"

# Wait for user to read intro
echo "Waiting 30 seconds to start. Ctrl+C to abort."
sleep 30

# Wait for user to configure repos.
echo "Configure your Ubuntu repositories to allow restricted, universe and multiverse repo. Waiting 10 seconds... Ctrl+C to abort."
sleep 10

# Update apt
echo "Updating apt repos..."
apt update

# Add ROS Noetic repo to sources.list.d/
echo "Adding ROS Noetic repos..."
echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list

# Add keys
echo "Installing curl..."
apt install curl

echo "Adding signing keys..."
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -

# Update repos
echo "Updating repos..."
apt update

# Install ROS
echo "Installing ROS..."
apt install ros-noetic-desktop-full

# Add ROS to .bashrc
echo "Adding ROS to .bashrc..."
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Add extra depends
echo "Installing extra dependencies..."
apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

echo "Install done! Restart bash to take effect."
