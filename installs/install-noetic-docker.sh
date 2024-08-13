echo "Game's ROS Noetic Installer"
echo "============================================="
echo "This is a script to quickly install ROS Noetic."
echo "The commands that will be run is to install Docker. You will need to configure and run the ROS container manually."
echo "This script should be RUN AS ROOT."
echo "(Copyright) Thapat A. GPLv3"

# Wait for user to read intro
echo "Waiting 30 seconds to start. Ctrl+C to abort."
sleep 30

# Remove other docker packages
echo "Removing unneeded Docker packages..."
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done

# Update apt
echo "Updating apt repos..."
apt-get update

# Install packages required to install
echo "Installing packages for installation..."
apt-get install ca-certificates curl

# Add GPG keys
echo "Adding keys..."
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add repos
echo "Adding repos..."

# Add the repository to Apt sources:
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update Repo
echo "Updating apt repos...
apt-get update

# Install Docker
echo "Installing Docker..."
apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
