#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "22481549"))
API_HASH     = os.environ.get("API_HASH", "e28d7a3cadcb4b191634f21329dd8084")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7006608206:AAHSbPU5_6p01O2FLtiZRlfCh0vACqr2dfM")
SESSION      = os.environ.get("SESSION", "BQDB-TfrKRztyGjUgy5JvURBWuljC664tCbBawFVFDAxTvXmHNWzUQKQ6BOwEzbtCsh4_Yi5zdVxoV1CQDoYyY7ZxsHJWViRdnP21XnK-IsefurimXW3F_FM9fhlUzyTGwbKMryrhg91_GbeP5wIrxJ78VpbP1r5jE2Zno_TakhGaU_88NAjnh4ZV8wG7F_Kx_p2pF9P0v2XqH5_7UqAJaCqLZnrWWCCdR8BpW8wzxW1Gpkn-xq29NAMupDZ7vGtCg94kDfLPgNnhpvt9-UG6JFDJ1BhqbXkCiJdAvBapIrdM1jc2-TLvwh1o1I4_kcSt_TfiR-m48-G-YBVkr73eoAAAAAaKbnskA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002000703839").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://destroyer48:aaaa11@destroyer48.3aydro7.mongodb.net/?retryWrites=true&w=majority&appName=destroyer48")
PORT         = os.environ.get("PORT", "8080")
