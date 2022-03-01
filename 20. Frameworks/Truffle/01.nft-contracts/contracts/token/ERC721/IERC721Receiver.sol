// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts v4.4.1 (token/ERC721/IERC721Receiver.sol)

pragma solidity ^0.8.0;

/**
 * @title ERC721 토큰 수신 인터페이스
 * @dev ERC721 asset contracts중에서 safeTransfers를 지원하고 싶은 모든 contract를 위한 인터페이스
 */
interface IERC721Receiver {
    /**
     * @dev `tokenId` 토큰이 `from`의 `operator`에 의해 
     * {IERC721-safeTransferFrom}을 통해 이 계약으로 전송될 때마다 이 함수가 호출됩니다.
     *
     * 토큰 전송을 확인하기 위해 Solidity selector를 반환해야 합니다.
     * 다른 값이 반환되거나 받는 사람이 인터페이스를 구현하지 않으면 이전이 취소됨.
     *
     * selector는 Solidity `IERC721Receiver.onERC721Received.selector`를 통해 얻을 수 있음
     */
    function onERC721Received(
        address operator,
        address from,
        uint256 tokenId,
        bytes calldata data
    ) external returns (bytes4);
}