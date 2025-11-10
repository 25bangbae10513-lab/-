import streamlit as st
import numpy as np

# 게임판 설정
BOARD_HEIGHT = 20
BOARD_WIDTH = 10

# 세션 상태 초기화
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
if 'current_block_pos' not in st.session_state:
    st.session_state.current_block_pos = [0, BOARD_WIDTH // 2 - 1]  # 블록 시작 위치

# 단순 2x2 블록
current_block = np.array([[1, 1],
                          [1, 1]])

def draw_board(board, block_pos):
    display = board.copy()
    y, x = block_pos
    # 블록 그리기
    for i in range(current_block.shape[0]):
        for j in range(current_block.shape[1]):
            if 0 <= y+i < BOARD_HEIGHT and 0 <= x+j < BOARD_WIDTH:
                display[y+i][x+j] = current_block[i][j]
    return display

st.title("Streamlit WASD 테트리스")

# 키 입력 받기
key = st.text_input("WASD 키 입력 (Enter 후 적용)").upper()

# 현재 블록 위치 업데이트
y, x = st.session_state.current_block_pos
if key == "A":
    x = max(0, x-1)
elif key == "D":
    x = min(BOARD_WIDTH - current_block.shape[1], x+1)
elif key == "S":
    y = min(BOARD_HEIGHT - current_block.shape[0], y+1)
elif key == "W":
    # 회전 구현 가능, 단순화 위해 아래로 한 칸 이동
    y = min(BOARD_HEIGHT - current_block.shape[0], y+1)

st.session_state.current_block_pos = [y, x]

# 게임판 그리기
board_display = draw_board(st.session_state.board, st.session_state.current_block_pos)
st.text(board_display)

# 아래로 자동 이동 (단순히 클릭으로 구현)
if st.button("블록 아래로 이동"):
    y = min(BOARD_HEIGHT - current_block.shape[0], st.session_state.current_block_pos[0]+1)
    st.session_state.current_block_pos[0] = y
