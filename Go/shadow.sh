#!/bin/bash

NET_DIR=/home/bstudent/fabric-samples/test-network
export FABRIC_CFG_PATH=${NET_DIR}/../config

export CORE_PEER_TLS_ENABLED=true
export ORDERER_CA=${NET_DIR}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem
export PEER0_ORG1_CA=${NET_DIR}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
export PEER0_ORG2_CA=${NET_DIR}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt

# 환경설정 함수 setEnv
setEnv() {
    ORG=$1
    if [ $ORG -eq 1 ]; then
        export CORE_PEER_LOCALMSPID="Org1MSP"
        export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG1_CA
        export CORE_PEER_MSPCONFIGPATH=${NET_DIR}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
        export CORE_PEER_ADDRESS=localhost:7051
    else
        export CORE_PEER_LOCALMSPID="Org2MSP"
        export CORE_PEER_TLS_ROOTCERT_FILE=$PEER0_ORG2_CA
        export CORE_PEER_MSPCONFIGPATH=${NET_DIR}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
        export CORE_PEER_ADDRESS=localhost:9051
    fi
}
set -ex
# package
peer lifecycle chaincode package asset.tar.gz --path /home/bstudent/dev/contract/ --lang golang --label asset_1.0

# org1 환경설정
setEnv 1
# install
peer lifecycle chaincode install asset.tar.gz

# org2 환경설정
setEnv 2
# install
peer lifecycle chaincode install asset.tar.gz

# queryinstall => id 추출을 위해서
peer lifecycle chaincode queryinstalled > qresult.txt
PACKAGE_ID=$(sed -n "/asset_1.0/{s/^Package ID: //; s/, Label:.*$//; p;}" qresult.txt)

# approvefororg
peer lifecycle chaincode approveformyorg -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA --channelID mychannel --name asset --version 1.0 --package-id ${PACKAGE_ID} --sequence 1

# org1 환경설정
setEnv 1
# approvefor org
peer lifecycle chaincode approveformyorg -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA --channelID mychannel --name asset --version 1.0 --package-id ${PACKAGE_ID} --sequence 1

# commit
peer lifecycle chaincode commit -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA --channelID mychannel --name asset --peerAddresses localhost:7051 --tlsRootCertFiles $PEER0_ORG1_CA --peerAddresses localhost:9051 --tlsRootCertFiles $PEER0_ORG2_CA --version 1.0 --sequence 1

peer lifecycle chaincode querycommitted -C mychannel -n asset

#invoke CreateAsset
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverride orderer.example.com --tls --cafile $ORDERER_CA --channelID mychannel --name asset --peerAddresses localhost:7051 --tlsRootCertFiles $PEER0_ORG1_CA --peerAddresses localhost:9051 --tlsRootCertFiles $PEER0_ORG2_CA -c '{"Args": 
["CreateAsset","asset100","skyblue","50","Kang","100000"]}'

#query ReadAsset

sleep 3

peer chaincode query -C mychannel -n asset -c '{"Args":["ReadAsset","asset100"]'
