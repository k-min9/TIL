var web3;  // web3 객체

// RPC URL 확인 위치 : Metamask -> 설정 -> 네트워크
const ROPSTEN_URL = 'https://ropsten.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161';
const CA = '0x69119966056DF42876DC3BCB7240Df0C3C24a317';
const STORAGE_ABI = [
            {
                "inputs": [],
                "name": "retrieve",
                "outputs": [
                    {
                        "internalType": "uint256",
                        "name": "",
                        "type": "uint256"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "uint256",
                        "name": "num",
                        "type": "uint256"
                    }
                ],
                "name": "store",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]
// 계정의 개인키. 서명에 사용 : 확인 위치 Metamask -> 계정정보보기 -> export private key -> 비밀번호 입력
const privateKey = 'e86e772a325842e5a76cb3990de53ef5e7f98829b117454d33420f4ca8de5481';
var sender;
var senderAddress;
var storageContract;

// 화면 로드시 web3 객체 생성 : Ropsten 네트워크의 RPC URL을 확인 후, 변수로 생성
// 이 시점에서 이 web3가 Ropsten 네트워크를 향한 web3임을 선언할 수 있음.
window.addEventListener('load', () => {
    if( typeof web3 !== 'undefined') {
        window.web3 = new Web3(web3.currentProvider);
        alert('web3 injected');
    } else {
        window.web3 = new Web3(new Web3.providers.HttpProvider(ROPSTEN_URL));
    }
    startApp();
});

// 계정 정보 생성 및 초기 값 세팅
function startApp() {
    // 1. 계정 정보
    sender = web3.eth.accounts.privateKeyToAccount('0x' + privateKey);
    // 2. contract 정보 (storage contract 인스턴스)
    storageContract = new web3.eth.Contract(STORAGE_ABI, CA);
    web3.eth.accounts.wallet.add(sender);
    web3.eth.defaultAccount = sender.address;
    senderAddress = web3.eth.defaultAccount;
    // 3. 화면에 초기 값 세팅
    document.getElementById('contractAddr').innerHTML = getAddrLink(CA);
    document.getElementById('accountAddr').innerHTML = getAddrLink(web3.eth.defaultAccount);
    retrieve();
}

function getAddrLink(addr) {
    return '<a target="_blank" href=https://ropsten.etherscan.io/address/' + addr + '>' + addr +'</a>';
}

function getTxLink(txHash) {
    return '<a target="_blank" href=https://ropsten.etherscan.io/tx/' + txHash + '>' + txHash +'</a>';
}

function getBlockLink(number) {
    return '<a target="_blank" href=https://ropsten.etherscan.io/block/' + number + '>' + number +'</a>';
}

/*
* call : 비용이 소요되지 않는 호출
* send : 트랜잭션 생성, 가스 필요
*/

// 찾아오기
function retrieve() {
    // 선언 Contract.methods.smartcontract내에서 선언한함수이름.call이라던가send이라던가
    storageContract.methods.retrieve().call({from: senderAddress})
    .then(result => {
        document.getElementById('storedData').innerHTML = result;
    });

    web3.eth.getBlockNumber(function(error, result){
        document.getElementById('lastBlock').innerHTML = getBlockLink(result);
    });
}

// 저장하기
function store() {
  let newValue = document.getElementById('newValue').value;

  storageContract.methods.store(newValue).estimateGas({ gas: 3000000 }, (error, gasAmount) => {
    storageContract.methods.store(newValue).send({
        from: senderAddress,
        gas: 3000000,
        gasPrice: 10000000000
    }).on("transactionHash", (hash) => {
        document.getElementById('txHash').innerHTML = getTxLink(hash);
    }).on("receipt", receipt => {
        if(receipt.status){
            retrieve();
        }
    }).on("error", (error, receipt) => {
        console.error(error);
        console.log(">> receipt: ", receipt);
    });
  });
  
}