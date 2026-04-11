class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix)-1
        while l < r:
            for i in range(r - l):
                t, b = l, r

                # save the topleft
                topleft = matrix[t][l+i]

                # move bl to tl
                matrix[t][l+i] = matrix[b-i][l]

                # move br to bl
                matrix[b-i][l] = matrix[b][r-i]

                # move tr to br
                matrix[b][r-i] = matrix[t+i][r]

                # move tl to tr
                matrix[t+i][r] = topleft
            r -= 1
            l += 1

        