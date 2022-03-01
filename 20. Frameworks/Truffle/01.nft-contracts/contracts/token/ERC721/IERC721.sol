// SPDX-License-Identifier: MIT
// OpenZeppelin Contracts v4.4.1 (token/ERC721/IERC721.sol)

pragma solidity ^0.8.0;

import "../../utils/introspection/IERC165.sol";

/**
 * @dev Required interface of an ERC721 compliant contract. : ERC721 호환 계약의 필수 인터페이스.
 */
interface IERC721 is IERC165 {
    /**
     * @dev `tokenId` 토큰이 `from`에서 `to`로 전송될 때 발생합니다.
     */
    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    /**
     * @dev Emitted when `owner` enables `approved` to manage the `tokenId` token.
     */
    event Approval(address indexed owner, address indexed approved, uint256 indexed tokenId);

    /**
     * @dev Emitted when `owner` enables or disables (`approved`) `operator` to manage all of its assets.
     */
    event ApprovalForAll(address indexed owner, address indexed operator, bool approved);

    /**
     * @dev  ``소유자``의 계정에 있는 토큰 수를 반환합니다.
     */
    function balanceOf(address owner) external view returns (uint256 balance);

    /**
     * @dev `tokenId` 토큰의 소유자를 반환합니다.
     * 요구사항 :`tokenId`
     */
    function ownerOf(uint256 tokenId) external view returns (address owner);

    /**
     * @dev `tokenId` 토큰을 `from`에서 `to`로 안전하게 전송,
     * 토큰이 영원히 잠기는 것을 방지하기 위해 계약 수신자가 ERC721 프로토콜을 알고 있는지 먼저 확인.
     *
     * 요구사항:
     *
     * - `from` cannot be the zero address.
     * - `to` cannot be the zero address.
     * - `tokenId` token must exist and be owned by `from`.
     * - If the caller is not `from`, {approve} 또는 {setApprovalForAll}에 의해 이 토큰을 이동할 수 있어야 함.
     * - If `to` refers to a smart contract, it must implement {IERC721Receiver-onERC721Received}, which is called upon a safe transfer.
     *
     * Emits a {Transfer} event.
     */
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;

    /**
     * @dev `tokenId` 토큰을 `from`에서 `to`로 전송합니다.
     *
     * WARNING: 가능하면 쓰지 말고, {safeTransferFrom} 쓸 것.
     *
     * Requirements:
     *
     * - `from` cannot be the zero address.
     * - `to` cannot be the zero address.
     * - `tokenId` token must be owned by `from`.
     * - If the caller is not `from`, it must be approved to move this token by either {approve} or {setApprovalForAll}.
     *
     * Emits a {Transfer} event.
     */
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) external;

    /**
     * @dev 'tokenId' 토큰을 다른 계정으로 전송하기 위해 'to'에 권한을 부여합니다.
     * The approval is cleared when the token is transferred.
     *
     * 한 번에 하나의 계정만 승인할 수 있으므로 제로 주소 승인은 이전 승인을 취소합니다.
     *
     * Requirements:
     *
     * - The caller must own the token or be an approved operator.
     * - `tokenId` must exist.
     *
     * Emits an {Approval} event.
     */
    function approve(address to, uint256 tokenId) external;

    /**
     * @dev `tokenId` 토큰에 대해 승인된 계정을 반환합니다.
     *
     * Requirements:
     *
     * - `tokenId` must exist.
     */
    function getApproved(uint256 tokenId) external view returns (address operator);

    /**
     * @dev Approve or remove `operator` as an operator for the caller.
     * Operators can call {transferFrom} or {safeTransferFrom} for any token owned by the caller.
     *
     * Requirements:
     *
     * - The `operator` cannot be the caller.
     *
     * Emits an {ApprovalForAll} event.
     */
    function setApprovalForAll(address operator, bool _approved) external;

    /**
     * @dev Returns if the `operator` is allowed to manage all of the assets of `owner`.
     *
     * See {setApprovalForAll}
     */
    function isApprovedForAll(address owner, address operator) external view returns (bool);

    /**
     * @dev `tokenId` 토큰을 `from`에서 `to`로 안전하게 전송.
     *
     * Requirements:
     *
     * - `from` cannot be the zero address.
     * - `to` cannot be the zero address.
     * - `tokenId` token must exist and be owned by `from`.
     * - If the caller is not `from`, it must be approved to move this token by either {approve} or {setApprovalForAll}.
     * - If `to` refers to a smart contract, it must implement {IERC721Receiver-onERC721Received}, which is called upon a safe transfer.
     *
     * Emits a {Transfer} event.
     */
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes calldata data
    ) external;
}