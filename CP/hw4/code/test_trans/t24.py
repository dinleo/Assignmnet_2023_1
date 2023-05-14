
*** Source Program **
def deep_flatten(a):
    res = []
    for x in a:
        if isinstance(x, int):
            res.append(x)
        else: 
            if isinstance(x, list):
                for t in deep_flatten(x):
                    res.append(t)




    return res

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,2,3],4,[[5,6],7,[[8,[9,10]],11]]]
print(deep_flatten(a))
print(deep_flatten(b))
print(deep_flatten([[[1,[1,2,3]],[2]],[[3],[4],[[1,2,3],[4,5,6,[[8,[9,10]],11]],[7,8,9]]]]))


*** Target Program **
  81 : def deep_flatten(a)
       5 : .t2 = []
       6 : res = .t2
       7 : .t6 = 0
       8 : __tidx__.t3 = .t6
       9 : .t7 = a
      10 : __titer__.t4 = .t7
      11 : .t9 = __titer__.t4
      12 : .t8 = len(.t9)
      13 : __tlen__.t5 = .t8
      14 : SKIP
      16 : .t11 = __tidx__.t3
      17 : .t12 = __tlen__.t5
      18 : .t10 = .t11 < .t12
      78 : iffalse .t10 goto 15
      19 : .t14 = __titer__.t4
      20 : .t15 = __tidx__.t3
      21 : .t13 = .t14[.t15]
      22 : x = .t13
      23 : .t17 = __tidx__.t3
      24 : .t18 = 1
      25 : .t16 = .t17 + .t18
      26 : __tidx__.t3 = .t16
      27 : .t20 = x
      28 : .t19 = isinstance(.t20, int)
      76 : if .t19 goto 70
      75 : goto 71
      70 : SKIP
      29 : .t22 = res
      30 : .t23 = x
      32 : .t21 = None
      31 : .t22 = .t22@[.t23]
      74 : goto 72
      71 : SKIP
      33 : .t25 = x
      34 : .t24 = isinstance(.t25, list)
      69 : if .t24 goto 63
      68 : goto 64
      63 : SKIP
      35 : .t29 = 0
      36 : __tidx__.t26 = .t29
      37 : .t31 = deep_flatten
      38 : .t32 = x
      39 : .t30 := call(.t31, (.t32))
      40 : __titer__.t27 = .t30
      41 : .t34 = __titer__.t27
      42 : .t33 = len(.t34)
      43 : __tlen__.t28 = .t33
      44 : SKIP
      46 : .t36 = __tidx__.t26
      47 : .t37 = __tlen__.t28
      48 : .t35 = .t36 < .t37
      62 : iffalse .t35 goto 45
      49 : .t39 = __titer__.t27
      50 : .t40 = __tidx__.t26
      51 : .t38 = .t39[.t40]
      52 : t = .t38
      53 : .t42 = __tidx__.t26
      54 : .t43 = 1
      55 : .t41 = .t42 + .t43
      56 : __tidx__.t26 = .t41
      57 : .t45 = res
      58 : .t46 = t
      60 : .t44 = None
      59 : .t45 = .t45@[.t46]
      61 : goto 44
      45 : SKIP
      67 : goto 65
      64 : SKIP
      66 : goto 65
      65 : SKIP
      73 : goto 72
      72 : SKIP
      77 : goto 14
      15 : SKIP
      79 : .t47 = res
      80 : return .t47
       3 : .t1 = None
       4 : return .t1

  82 : .t50 = 1
  83 : .t52 = 2
  84 : .t54 = 3
  85 : .t55 = []
  86 : .t55 = .t54::.t55
  87 : .t53 = .t55
  88 : .t53 = .t52::.t53
  89 : .t51 = .t53
  90 : .t51 = .t50::.t51
  91 : .t49 = .t51
  92 : .t58 = 4
  93 : .t60 = 5
  94 : .t62 = 6
  95 : .t63 = []
  96 : .t63 = .t62::.t63
  97 : .t61 = .t63
  98 : .t61 = .t60::.t61
  99 : .t59 = .t61
 100 : .t59 = .t58::.t59
 101 : .t57 = .t59
 102 : .t66 = 7
 103 : .t68 = 8
 104 : .t70 = 9
 105 : .t71 = []
 106 : .t71 = .t70::.t71
 107 : .t69 = .t71
 108 : .t69 = .t68::.t69
 109 : .t67 = .t69
 110 : .t67 = .t66::.t67
 111 : .t65 = .t67
 112 : .t72 = []
 113 : .t72 = .t65::.t72
 114 : .t64 = .t72
 115 : .t64 = .t57::.t64
 116 : .t56 = .t64
 117 : .t56 = .t49::.t56
 118 : .t48 = .t56
 119 : a = .t48
 120 : .t75 = 1
 121 : .t77 = 2
 122 : .t79 = 3
 123 : .t80 = []
 124 : .t80 = .t79::.t80
 125 : .t78 = .t80
 126 : .t78 = .t77::.t78
 127 : .t76 = .t78
 128 : .t76 = .t75::.t76
 129 : .t74 = .t76
 130 : .t82 = 4
 131 : .t86 = 5
 132 : .t88 = 6
 133 : .t89 = []
 134 : .t89 = .t88::.t89
 135 : .t87 = .t89
 136 : .t87 = .t86::.t87
 137 : .t85 = .t87
 138 : .t91 = 7
 139 : .t95 = 8
 140 : .t98 = 9
 141 : .t100 = 10
 142 : .t101 = []
 143 : .t101 = .t100::.t101
 144 : .t99 = .t101
 145 : .t99 = .t98::.t99
 146 : .t97 = .t99
 147 : .t102 = []
 148 : .t102 = .t97::.t102
 149 : .t96 = .t102
 150 : .t96 = .t95::.t96
 151 : .t94 = .t96
 152 : .t104 = 11
 153 : .t105 = []
 154 : .t105 = .t104::.t105
 155 : .t103 = .t105
 156 : .t103 = .t94::.t103
 157 : .t93 = .t103
 158 : .t106 = []
 159 : .t106 = .t93::.t106
 160 : .t92 = .t106
 161 : .t92 = .t91::.t92
 162 : .t90 = .t92
 163 : .t90 = .t85::.t90
 164 : .t84 = .t90
 165 : .t107 = []
 166 : .t107 = .t84::.t107
 167 : .t83 = .t107
 168 : .t83 = .t82::.t83
 169 : .t81 = .t83
 170 : .t81 = .t74::.t81
 171 : .t73 = .t81
 172 : b = .t73
 173 : .t110 = deep_flatten
 174 : .t111 = a
 175 : .t109 := call(.t110, (.t111))
 176 : .t112 = " "
 178 : write .t109
 177 : write .t112
 179 : .t113 = "\n"
 180 : write .t113
 181 : .t108 = None
 182 : .t116 = deep_flatten
 183 : .t117 = b
 184 : .t115 := call(.t116, (.t117))
 185 : .t118 = " "
 187 : write .t115
 186 : write .t118
 188 : .t119 = "\n"
 189 : write .t119
 190 : .t114 = None
 191 : .t122 = deep_flatten
 192 : .t126 = 1
 193 : .t129 = 1
 194 : .t131 = 2
 195 : .t133 = 3
 196 : .t134 = []
 197 : .t134 = .t133::.t134
 198 : .t132 = .t134
 199 : .t132 = .t131::.t132
 200 : .t130 = .t132
 201 : .t130 = .t129::.t130
 202 : .t128 = .t130
 203 : .t135 = []
 204 : .t135 = .t128::.t135
 205 : .t127 = .t135
 206 : .t127 = .t126::.t127
 207 : .t125 = .t127
 208 : .t138 = 2
 209 : .t139 = []
 210 : .t139 = .t138::.t139
 211 : .t137 = .t139
 212 : .t140 = []
 213 : .t140 = .t137::.t140
 214 : .t136 = .t140
 215 : .t136 = .t125::.t136
 216 : .t124 = .t136
 217 : .t144 = 3
 218 : .t145 = []
 219 : .t145 = .t144::.t145
 220 : .t143 = .t145
 221 : .t148 = 4
 222 : .t149 = []
 223 : .t149 = .t148::.t149
 224 : .t147 = .t149
 225 : .t153 = 1
 226 : .t155 = 2
 227 : .t157 = 3
 228 : .t158 = []
 229 : .t158 = .t157::.t158
 230 : .t156 = .t158
 231 : .t156 = .t155::.t156
 232 : .t154 = .t156
 233 : .t154 = .t153::.t154
 234 : .t152 = .t154
 235 : .t161 = 4
 236 : .t163 = 5
 237 : .t165 = 6
 238 : .t169 = 8
 239 : .t172 = 9
 240 : .t174 = 10
 241 : .t175 = []
 242 : .t175 = .t174::.t175
 243 : .t173 = .t175
 244 : .t173 = .t172::.t173
 245 : .t171 = .t173
 246 : .t176 = []
 247 : .t176 = .t171::.t176
 248 : .t170 = .t176
 249 : .t170 = .t169::.t170
 250 : .t168 = .t170
 251 : .t178 = 11
 252 : .t179 = []
 253 : .t179 = .t178::.t179
 254 : .t177 = .t179
 255 : .t177 = .t168::.t177
 256 : .t167 = .t177
 257 : .t180 = []
 258 : .t180 = .t167::.t180
 259 : .t166 = .t180
 260 : .t166 = .t165::.t166
 261 : .t164 = .t166
 262 : .t164 = .t163::.t164
 263 : .t162 = .t164
 264 : .t162 = .t161::.t162
 265 : .t160 = .t162
 266 : .t183 = 7
 267 : .t185 = 8
 268 : .t187 = 9
 269 : .t188 = []
 270 : .t188 = .t187::.t188
 271 : .t186 = .t188
 272 : .t186 = .t185::.t186
 273 : .t184 = .t186
 274 : .t184 = .t183::.t184
 275 : .t182 = .t184
 276 : .t189 = []
 277 : .t189 = .t182::.t189
 278 : .t181 = .t189
 279 : .t181 = .t160::.t181
 280 : .t159 = .t181
 281 : .t159 = .t152::.t159
 282 : .t151 = .t159
 283 : .t190 = []
 284 : .t190 = .t151::.t190
 285 : .t150 = .t190
 286 : .t150 = .t147::.t150
 287 : .t146 = .t150
 288 : .t146 = .t143::.t146
 289 : .t142 = .t146
 290 : .t191 = []
 291 : .t191 = .t142::.t191
 292 : .t141 = .t191
 293 : .t141 = .t124::.t141
 294 : .t123 = .t141
 295 : .t121 := call(.t122, (.t123))
 296 : .t192 = " "
 298 : write .t121
 297 : write .t192
 299 : .t193 = "\n"
 300 : write .t193
 301 : .t120 = None
   2 : HALT

[1, 2, 3, 4, 5, 6, 7, 8, 9] 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
[1, 1, 2, 3, 2, 3, 4, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 7, 8, 9] 
The number of instructions executed : 4300