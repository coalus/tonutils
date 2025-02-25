from __future__ import annotations

from typing import Optional

from pytoniq_core import Cell, begin_cell, Address

from ..base.nft import NFT
from ...data import NFTData
from ...op_codes import *


class NFTSoulbound(NFT):
    CODE_HEX = "b5ee9c724102130100033b000114ff00f4a413f4bcf2c80b0102016202030202ce04050201200f1004bd46c2220c700915be001d0d303fa4030f002f842b38e1c31f84301c705f2e195fa4001f864d401f866fa4030f86570f867f003e002d31f0271b0e30201d33f8210d0c3bfea5230bae302821004ded1485230bae3023082102fcb26a25220ba8060708090201200d0e00943031d31f82100524c7ae12ba8e39d33f308010f844708210c18e86d255036d804003c8cb1f12cb3f216eb39301cf179131e2c97105c8cb055004cf1658fa0213cb6accc901fb009130e200c26c12fa40d4d30030f847f841c8cbff5006cf16f844cf1612cc14cb3f5230cb0003c30096f8465003cc02de801078b17082100dd607e3403514804003c8cb1f12cb3f216eb39301cf179131e2c97105c8cb055004cf1658fa0213cb6accc901fb0000c632f8445003c705f2e191fa40d4d30030f847f841c8cbfff844cf1613cc12cb3f5210cb0001c30094f84601ccde801078b17082100524c7ae405503804003c8cb1f12cb3f216eb39301cf179131e2c97105c8cb055004cf1658fa0213cb6accc901fb0003fa8e4031f841c8cbfff843cf1680107082108b7717354015504403804003c8cb1f12cb3f216eb39301cf179131e2c97105c8cb055004cf1658fa0213cb6accc901fb00e082101f04537a5220bae30282106f89f5e35220ba8e165bf84501c705f2e191f847c000f2e193f823f867f003e08210d136d3b35220bae30230310a0b0c009231f84422c705f2e1918010708210d53276db102455026d830603c8cb1f12cb3f216eb39301cf179131e2c97105c8cb055004cf1658fa0213cb6accc901fb008b02f8648b02f865f003008e31f84422c705f2e191820afaf08070fb028010708210d53276db102455026d830603c8cb1f12cb3f216eb39301cf179131e2c97105c8cb055004cf1658fa0213cb6accc901fb00002082105fcc3d14ba93f2c19dde840ff2f000613b513434cfc07e187e90007e18dc3e188835d2708023859ffe18be90007e1935007e19be90007e1974cfcc3e19e44c38a000373e11fe11be107232cffe10f3c5be1133c5b33e1173c5b2cff27b55200201581112001dbc7e7f8017c217c20fc21fc227c234000db5631e005f08b0000db7b07e005f08f02d32a570"  # noqa

    def __init__(
            self,
            index: int,
            collection_address: Address,
    ) -> None:
        self._data = self.create_data(index, collection_address).serialize()
        self._code = Cell.one_from_boc(self.CODE_HEX)

    @classmethod
    def create_data(
            cls,
            index: int,
            collection_address: Address,
    ) -> NFTData:
        return NFTData(
            index=index,
            collection_address=collection_address,
        )

    @classmethod
    def build_revoke_body(cls, query_id: int = 0) -> Cell:
        """
        Builds the body of the revoke nft transaction.

        :param query_id: The query ID. Defaults to 0.
        :param query_id: int, optional
        :return: The cell representing the body of the revoke nft transaction.
        """
        return (
            begin_cell()
            .store_uint(REVOKE_NFT_OPCODE, 32)
            .store_uint(query_id, 64)
            .end_cell()
        )

    @classmethod
    def build_destroy_body(cls, query_id: int = 0) -> Cell:
        """
        Builds the body of the destroy nft transaction.

        :param query_id: The query ID. Defaults to 0.
        :param query_id: int, optional
        :return: The cell representing the body of the destroy nft transaction.
        """
        return (
            begin_cell()
            .store_uint(DESTROY_NFT_OPCODE, 32)
            .store_uint(query_id, 64)
            .end_cell()
        )

    @classmethod
    def build_transfer_body(
            cls,
            new_owner_address: Address,
            response_address: Optional[Address] = None,
            custom_payload: Optional[Cell] = None,
            forward_payload: Optional[Cell] = None,
            forward_amount: int = 0,
            query_id: int = 0,
    ) -> Cell:
        raise NotImplementedError("`Transfer nft` is not supported in the SoulBound NFT Contract.")
