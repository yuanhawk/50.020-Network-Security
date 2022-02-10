#include <unistd.h>
#include <stdio.h>
#include <sys/socket.h>
#include <linux/if_packet.h>
#include <net/ethernet.h>
#include <arpa/inet.h>
#include <stdlib.h>

int main() {
    int PACKET_LEN = 512;
    char buffer[PACKET_LEN];
    struct sockaddr saddr;
    struct packet_mreq mr;
    int def = -1;

    // Create the raw socket
    int sock = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL)); 
    
    // Turn off the promiscuous mode.
    // mr.mr_type = PACKET_MR_PROMISC;
    setsockopt(sock, SOL_PACKET, PACKET_ADD_MEMBERSHIP, &mr, sizeof(mr));

    // Getting captured packets
    int data_size=recvfrom(sock, buffer, PACKET_LEN, 0, 
                     &saddr, (socklen_t*)sizeof(saddr));
    if(data_size) printf("Got one packet\n");

    // Turn on the promiscuous mode.
    mr.mr_type = PACKET_MR_PROMISC;
    setsockopt(sock, SOL_PACKET, PACKET_ADD_MEMBERSHIP, &mr, sizeof(mr));

    // Getting captured packets
    data_size=recvfrom(sock, buffer, PACKET_LEN, 0,
                     &saddr, (socklen_t*)sizeof(saddr));
    if(data_size) printf("Got one packet\n");

    close(sock);
    return 0;
}
