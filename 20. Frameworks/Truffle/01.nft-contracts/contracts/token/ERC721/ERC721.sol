// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts (last updated v4.5.0) (token/ERC721/ERC721.sol)

pragma solidity ^0.8.4;

import "./IERC721.sol";
import "./IERC721Receiver.sol";
import "./extensions/IERC721Metadata.sol";
import "../../utils/Address.sol";
import "../../utils/Context.sol";
import "../../utils/Strings.sol";
import "../../utils/introspection/ERC165.sol";

/**
 * @dev EIP-721을 준수한 ERC-721 구현 ({ERCEnumerable} 제외)
 * https://eips.ethereum.org/EIPS/eip-721[ERC721]
 */
contract ERC721 is Context, ERC165, IERC721, IERC721Metadata {
    using Address for address;
    using Strings for uint256;

    // 토큰 이름
    string private _name;

    // 토큰 심볼(단위)
    string private _symbol;

    // Mapping : 토큰 소유자
    mapping(uint256 => address) private _owners;

    // Mapping : 소유자 주소 => 토큰 수
    mapping(address => uint256) private _balances;

    // Mapping : 토큰 ID => approved address
    mapping(uint256 => address) private _tokenApprovals;

    // Mapping : 부여된 토큰 operator 및 권한 정보
    mapping(address => mapping(address => bool)) private _operatorApprovals;

    /**
     * @dev `name`과 `symbol`을 사용한 생성자. 정상동작시 컨트랙트주소에 따른 고유성이 보장되나, 혼동을 피하기 위해 고유 이름 및 심볼 사용 권장
     */
    constructor(string memory name_, string memory symbol_) {
        _name = name_;
        _symbol = symbol_;
    }

    /**
     * @dev ERC-721이 반드시 구현해야할 함수를 구현하고 있는지 판별
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC165, IERC165) returns (bool) {
        return
        //솔리디티 type을 이용해 구현
            interfaceId == type(IERC721).interfaceId ||
            interfaceId == type(IERC721Metadata).interfaceId ||
            super.supportsInterface(interfaceId);
    }

    /**
     * @dev 특정 주소가 몇 개의 NFT 토큰을 보유하는지 반환
     */
    function balanceOf(address owner) public view virtual override returns (uint256) {
        require(owner != address(0), "ERC721: balance query for the zero address");  // 매개변수는 0주소일 수 없습니다.
        return _balances[owner];
    }

    /**
     * @dev 특정 토큰의 소유자 주소를 반환
     */
    function ownerOf(uint256 tokenId) public view virtual override returns (address) {
        address owner = _owners[tokenId];
        require(owner != address(0), "ERC721: owner query for nonexistent token");
        return owner;
    }

    /**
     * @dev IERC721Metadata 상태변수 name 반환
     */
    function name() public view virtual override returns (string memory) {
        return _name;
    }

    /**
     * @dev IERC721Metadata 상태변수 symbol 반환
     */
    function symbol() public view virtual override returns (string memory) {
        return _symbol;
    }

    /**
     * @dev IERC721Metadata 상태변수 tokenURI 반환
     */
    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");

        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 ? string(abi.encodePacked(baseURI, tokenId.toString())) : "";
    }

    /**
     * @dev Base URI for computing {tokenURI}. If set, the resulting URI for each
     * token will be the concatenation of the `baseURI` and the `tokenId`. Empty
     * by default, can be overridden in child contracts.
     */
    function _baseURI() internal view virtual returns (string memory) {
        return "";
    }

    /**
     * @dev 토큰 권한을 특정 주소에 부여
     */
    function approve(address to, uint256 tokenId) public virtual override {
        address owner = ERC721.ownerOf(tokenId);
        // NFT 소유자만 권한 부여할 수 있어야함
        require(to != owner, "ERC721: approval to current owner");

        require(
            _msgSender() == owner || isApprovedForAll(owner, _msgSender()),
            "ERC721: approve caller is not owner nor approved for all"
        );

        // 권한 부여시 Approval 이벤트 발생
        _approve(to, tokenId);
    }

    /**
     * @dev 토큰의 approve 권한을 가진 주소를 반환
     */
    function getApproved(uint256 tokenId) public view virtual override returns (address) {
        require(_exists(tokenId), "ERC721: approved query for nonexistent token");

        return _tokenApprovals[tokenId];
    }

    /**
     * @dev 토큰의 operator를 설정.
     * operator : 특정 소유자의 토큰을 전송할 수 있는 모든 권한을 가짐
     */
    function setApprovalForAll(address operator, bool approved) public virtual override {
        _setApprovalForAll(_msgSender(), operator, approved);
    }

    /**
     * @dev 특정 주소가 operator 권한을 갖는지 반환
     */
    function isApprovedForAll(address owner, address operator) public view virtual override returns (bool) {
        return _operatorApprovals[owner][operator];
    }

    /**
     * @dev transferFrom.
     */
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public virtual override {
        //solhint-disable-next-line max-line-length
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: transfer caller is not owner nor approved");

        _transfer(from, to, tokenId);
    }

    /**
     * @dev _data를 ""로 바꾼 safeTransferFrom.
     */
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public virtual override {
        safeTransferFrom(from, to, tokenId, "");
    }

    /**
     * @dev NFT 전송함수 : ERC-20으로 구매하는 상황을 상정할 경우 payable은 불필요.
     */
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes memory _data
    ) public virtual override {
        // 송금 지시할 수 있는 대상 : NFT의 소유 당사자나 승인 받은 주소, 지정된 관리자 주소
        require(_isApprovedOrOwner(_msgSender(), tokenId), "ERC721: transfer caller is not owner nor approved");
        _safeTransfer(from, to, tokenId, _data);
    }

    /**
     * @dev `tokenId` 토큰을 `from`에서 `to`로 안전하게 전송,
     * 토큰이 영원히 잠기는 것을 방지하기 위해 계약 수신자가 ERC721 프로토콜을 알고 있는지 먼저 확인.
     *
     * _data`는 추가 데이터로 지정된 형식이 없으며 `to`를 호출하여 전송
     *
     * 이 내부 함수는 {safeTransferFrom}과 동일하며
     * 예를 들어 서명 기반과 같은 토큰 전송을 수행하는 대체 메커니즘을 구현
     *
     * Requirements:
     *
     * - `from` cannot be the zero address.
     * - `to` cannot be the zero address.
     * - `tokenId` token must exist and be owned by `from`.
     * - If `to` refers to a smart contract, it must implement {IERC721Receiver-onERC721Received}, which is called upon a safe transfer.
     *
     * Emits a {Transfer} event.
     */
    function _safeTransfer(
        address from,
        address to,
        uint256 tokenId,
        bytes memory _data
    ) internal virtual {
        _transfer(from, to, tokenId);
        // transferFrom과 가장 큰 차이 : 받는 주소가 스마트 컨트랙트 주소인 경우, ERC721Reciver의 onERC721Recieved가 구현되어있는지 확인
        require(_checkOnERC721Received(from, to, tokenId, _data), "ERC721: transfer to non ERC721Receiver implementer");
    }

    /**
     * @dev Returns whether `tokenId` exists.
     *
     * Tokens can be managed by their owner or approved accounts via {approve} or {setApprovalForAll}.
     *
     * Tokens start existing when they are minted (`_mint`),
     * and stop existing when they are burned (`_burn`).
     */
    function _exists(uint256 tokenId) internal view virtual returns (bool) {
        return _owners[tokenId] != address(0);
    }

    /**
     * @dev Returns whether `spender` is allowed to manage `tokenId`.
     *
     * Requirements:
     *
     * - `tokenId` must exist.
     */
    function _isApprovedOrOwner(address spender, uint256 tokenId) internal view virtual returns (bool) {
        require(_exists(tokenId), "ERC721: operator query for nonexistent token");  // 유효한 토큰 ID인지 확인
        address owner = ERC721.ownerOf(tokenId);
        return (spender == owner || getApproved(tokenId) == spender || isApprovedForAll(owner, spender));
    }

    /**
     * @dev 새로운 NFT를 생성하는 함수(mint)의 safe 버전
     *
     * Requirements:
     *
     * - `tokenId` must not exist.
     * - If `to` refers to a smart contract, it must implement {IERC721Receiver-onERC721Received}, which is called upon a safe transfer.
     *
     * Emits a {Transfer} event.
     */
    function _safeMint(address to, uint256 tokenId) internal virtual {
        _safeMint(to, tokenId, "");
    }

    /**
     * @dev Same as {xref-ERC721-_safeMint-address-uint256-}[`_safeMint`], with an additional `data` parameter which is
     * forwarded in {IERC721Receiver-onERC721Received} to contract recipients.
     * 새로운 NFT를 생성하는 함수(mint)의 safe 버전
     */
    function _safeMint(
        address to,
        uint256 tokenId,
        bytes memory _data
    ) internal virtual {
        _mint(to, tokenId);
        require(
            _checkOnERC721Received(address(0), to, tokenId, _data),
            "ERC721: transfer to non ERC721Receiver implementer"
        );
    }

    /**
     * @dev 새로운 NFT를 생성하는 함수
     *
     * WARNING: 비추천, 가능하면 {_safeMint} 쓸 것
     *
     * Requirements:
     *
     * - `tokenId` must not exist.
     * - `to` cannot be the zero address.
     *
     * Emits a {Transfer} event.
     */
    function _mint(address to, uint256 tokenId) internal virtual {
        require(to != address(0), "ERC721: mint to the zero address");
        require(!_exists(tokenId), "ERC721: token already minted");

        // contract 시점을 hooking 할 수 있는게 EIP-165 특징 중 하나
        _beforeTokenTransfer(address(0), to, tokenId);

        _balances[to] += 1;
        _owners[tokenId] = to;

        emit Transfer(address(0), to, tokenId);

        // contract 시점을 hooking 할 수 있는게 EIP-165 특징 중 하나
        _afterTokenTransfer(address(0), to, tokenId);
    }

    /**
     * @dev NFT를 소각(삭제) 하는 함수
     * The approval is cleared when the token is burned.
     *
     * Requirements:
     *
     * - `tokenId` must exist.
     *
     * Emits a {Transfer} event.
     */
    function _burn(uint256 tokenId) internal virtual {
        address owner = ERC721.ownerOf(tokenId);


        // contract 시점을 hooking 할 수 있는게 EIP-165 특징 중 하나
        _beforeTokenTransfer(owner, address(0), tokenId);

        // Clear approvals
        _approve(address(0), tokenId);

        _balances[owner] -= 1;
        delete _owners[tokenId];

        emit Transfer(owner, address(0), tokenId);

        // contract 시점을 hooking 할 수 있는게 EIP-165 특징 중 하나
        _afterTokenTransfer(owner, address(0), tokenId);
    }

    /**
     * @dev `tokenId`를 `from`에서 `to`로 전송합니다.
     *  {transferFrom}과 달리 msg.sender에 제한이 없습니다.
     *
     * Requirements:
     * - `to` cannot be the zero address.
     * - `tokenId` token must be owned by `from`.
     *
     * Emits a {Transfer} event.
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual {
        require(ERC721.ownerOf(tokenId) == from, "ERC721: transfer from incorrect owner");
        require(to != address(0), "ERC721: transfer to the zero address");

        // contract 시점을 hooking 할 수 있는게 EIP-165 특징 중 하나
        _beforeTokenTransfer(from, to, tokenId);

        // 전 주인의 approval 지우기
        _approve(address(0), tokenId);

        // 대상의 balance 조절
        _balances[from] -= 1;
        _balances[to] += 1;
        _owners[tokenId] = to;

        emit Transfer(from, to, tokenId);

        // contract 시점을 hooking 할 수 있는게 EIP-165 특징 중 하나
        _afterTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Approve `to` to operate on `tokenId`
     *
     * Emits a {Approval} event.
     */
    function _approve(address to, uint256 tokenId) internal virtual {
        _tokenApprovals[tokenId] = to;
        emit Approval(ERC721.ownerOf(tokenId), to, tokenId);
    }

    /**
     * @dev 토큰의 operator를 설정.
     * operator : 특정 소유자의 토큰을 전송할 수 있는 모든 권한을 가짐
     *
     * Emits a {ApprovalForAll} event.
     */
    function _setApprovalForAll(
        address owner,
        address operator,
        bool approved
    ) internal virtual {
        require(owner != operator, "ERC721: approve to caller");
        _operatorApprovals[owner][operator] = approved;  // 토큰 소유자에 의해서만 지정 가능
        emit ApprovalForAll(owner, operator, approved);
    }

    /**
     * @dev Internal function to invoke {IERC721Receiver-onERC721Received} on a target address.
     * The call is not executed if the target address is not a contract.
     *
     * @param from address representing the previous owner of the given token ID
     * @param to target address that will receive the tokens
     * @param tokenId uint256 ID of the token to be transferred
     * @param _data bytes optional data to send along with the call
     * @return bool whether the call correctly returned the expected magic value
     */
    function _checkOnERC721Received(
        address from,
        address to,
        uint256 tokenId,
        bytes memory _data
    ) private returns (bool) {
        // safetransferFrom과 transferFrom과의 가장 큰 차이
        // 받는 주소가 스마트 컨트랙트 주소인 경우, ERC721Reciver의 onERC721Recieved가 구현되어있는지 확인
        if (to.isContract()) {
            try IERC721Receiver(to).onERC721Received(_msgSender(), from, tokenId, _data) returns (bytes4 retval) {
                return retval == IERC721Receiver.onERC721Received.selector;
            } catch (bytes memory reason) {
                if (reason.length == 0) {
                    revert("ERC721: transfer to non ERC721Receiver implementer");
                } else {
                    assembly {
                        revert(add(32, reason), mload(reason))
                    }
                }
            }
        } else {
            return true;
        }
    }

    /**
     * @dev Hook that is called before any token transfer. This includes minting
     * and burning.
     *
     * Calling conditions:
     *
     * - When `from` and `to` are both non-zero, ``from``'s `tokenId` will be
     * transferred to `to`.
     * - When `from` is zero, `tokenId` will be minted for `to`.
     * - When `to` is zero, ``from``'s `tokenId` will be burned.
     * - `from` and `to` are never both zero.
     *
     * To learn more about hooks, head to xref:ROOT:extending-contracts.adoc#using-hooks[Using Hooks].
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual {}

    /**
     * @dev Hook that is called after any transfer of tokens. This includes
     * minting and burning.
     *
     * Calling conditions:
     *
     * - when `from` and `to` are both non-zero.
     * - `from` and `to` are never both zero.
     *
     * To learn more about hooks, head to xref:ROOT:extending-contracts.adoc#using-hooks[Using Hooks].
     */
    function _afterTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal virtual {}
}