
# # export midi track as .png
# plot_midi(downscaled_notes,filename = "miditester_temp")
# plot_midi(notes_np,filename = "raw_first_1024")

# ## DRAW NOTES USING MATPLOTLIB

# ss_l = 1024
# v_l = 129
# ss = downscaled_notes[:ss_l]
# y = [i if ss[e][i] else float("nan") for e in range(ss_l) for i in range(v_l)]
# fig, ax = plt.subplots(figsize = (40,10))
# t = [x for x in range(ss_l)]*v_l
# t.sort()
# ax.plot(t, y, 'ko', markersize=2)

# ax.set(xlabel='time (tick)', ylabel='note',
#        title='')
# ax.grid()

# print("Saving fig")
# plt.savefig('test_high_res.png', dpi=500)
# print("Done with fig. Showing fig")
# #plt.show()


# print()


# # draw notes like in garage band: USING NOTES OBJECTS
# pygame.init()
# screen = pygame.display.set_mode((800, 128*2))
# clock = pygame.time.Clock()

# done = False

# print("Entering loop")
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     #draw first 2000
#     screen.fill((0, 0, 0))  
#     color = (255,0,0)

#     scale_x = 10
#     for note_obj in notes:
#         y = (128*2) - (note_obj.note * 2)
#         x1 = note_obj.start_time / scale_x
#         x2 = note_obj.stop_time / scale_x
#         pygame.draw.line(screen,color,(x1,y),(x2,y))

#     #for point in getLine((200,200),(mouse_x,mouse_y)):
#     #    pygame.draw.line(screen,(255,255,255),point,point)

#     pygame.display.flip()       
#     clock.tick(120)

#####################################################################

# # draw notes like in garage band: USING NUMPY ARRAY
# pygame.init()
# screen = pygame.display.set_mode((1600, 128*2))
# clock = pygame.time.Clock()

# done = False

# print("Entering loop")
# once = True
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     if once:
#         #draw first 2000
#         screen.fill((0, 0, 0))  
#         color = (255,0,0)

#         scale_x = 10
#         for time, vector in enumerate(notes_num):
#             for note, is_active in enumerate(vector):
#                 if is_active:
#                     y = (128*2) - (note * 2)
#                     pygame.draw.line(screen,color,(time/scale_x,y),(time/scale_x,y))

#         #for point in getLine((200,200),(mouse_x,mouse_y)):
#         #    pygame.draw.line(screen,(255,255,255),point,point)
#         once = False

#     pygame.display.flip()       
#     clock.tick(120)

########################################################

# # draw notes like in garage band: USING NUMPY ARRAY WITH COMPARISON TO DOWNSCALED
# pygame.init()
# screen = pygame.display.set_mode((1600, 128*2))
# clock = pygame.time.Clock()

# done = False

# print("Entering loop")
# once = True
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#     if once:
#         #draw first 2000
#         screen.fill((0, 0, 0))  
#         color = (255,0,0)

#         scale_x = 10
#         for time, vector in enumerate(notes_np):
#             for note, is_active in enumerate(vector):
#                 if is_active:
#                     y = (128*2) - (note * 2)
#                     pygame.draw.line(screen,color,(time/scale_x,y),(time/scale_x,y))

#         scale_x = 0.1
#         for time, vector in enumerate(downscaled_notes):
#             for note, is_active in enumerate(vector):
#                 if is_active:
#                     y = ((128*2) - (note * 2)) + 2
#                     pygame.draw.line(screen,(0,255,0),(time/scale_x,y),(time/scale_x,y))

#         #for point in getLine((200,200),(mouse_x,mouse_y)):
#         #    pygame.draw.line(screen,(255,255,255),point,point)
#         once = False

#     pygame.display.flip()       
#     clock.tick(120)

