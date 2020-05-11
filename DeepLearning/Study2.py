#여태까지는 하나의 input에 대해 결과를 예측하였지만 이제는 여러개의 input에 대해 예측을 해보자
# input이 1개일땐, H(x) = W*x+b였었는데 3개면 어떻게할까?? 단순하게 H(x1,x2,x3) = w1*x1+w2*x2+w3*x3+b 해주면 된다.
# cost역시 (H(x1,x2,x3)-y)^2 /m 해주면 되는거, 만일 H(x)에 input이 너무 많아지면 matrix 곱을 이용하면 된다. 보통 matrix를 쓸때는 H(X)=WX라 쓰지않고 XW라 쓴다.그리고 크게 대문자라고 쓴것도 matrix라는 뜻이다
#Matrix를 쓸땐 H(X)=XW다.ex)[5,3]*[3,1]=[5,1] 반드시 이연산을 할땐 앞행렬에 뒤자리와 뒷행렬에 앞자리가 같아야 하며 그 같은 수를 지우면 나오는게 곱해서 나오는 matrix다,그래서 우리가 입력을 해줄땐, 그 데이터의 행,렬에 맞춰 [5,3], [3,1] 이런식으로 입력해준다.
#[5,3] 여기서 5은 우리가 데이터을 몇 개를 넣은것인가하는 인스턴스의 갯수이고, 3은 x의 variable의 갯수, 개수를 봤을때[None,3]이면 데이터의 개수가 몇개들어오든 상관없다 라는 뜻


########################과연 tensorflow는 어떻게 배울고,학습할까?? 이방법은 내가 나중에 gradient(경사)를 내가 따로 바꾸고싶다면 ###########################################
# import tensorflow as tf
#
# X = [1,2,3]
# Y = [1,2,3]
#
# W = tf.Variable(5.0)
# hypo = X*W
# cost = tf.reduce_mean(tf.square(hypo-Y))
# gradient = tf.reduce_mean((W*X-Y)*X)*2 #전 예제에서 사용한 미분한 값인데 우리가 저렇게 gradient를 조정해서 과연 이 미분값과 같은지 테스트용으로 적어준것
# optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
# #원래대로라면 optimizer에게 학습하는걸 알려준후, cost를 minimize해줘야하지만 그렇게 해주지않고,이 cost에 맞는gradient를 계산해달라고한다.
# gvs = optimizer.compute_gradients(cost,[W])#gradient는 계산한 값, 수정가능함
# apply_gradient = optimizer.apply_gradients(gvs) #이 gvs라는 값을 사용,적용  할수있다
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
#
# for i in range(100):
#     print(i,sess.run([gradient,W,gvs])) # gvs는  W과 gradient를 같이 보여준다.
#     sess.run(apply_gradient)

###########################경사하강알고리즘을 수동으로 적을떄, sess.run(train)은 말그대로 학습을 시켜주는것 -> 한번씩 경사면에서 한발씩떼면서 최적의 값으로 움직이는거라고 생각하면됌
# import tensorflow as tf
# Xdata = [1,2,3]
# Ydata = [1,2,3]
#
# W = tf.Variable(tf.random_normal([1]),name="weight")
# X = tf.placeholder(tf.float32)
# Y = tf.placeholder(tf.float32)
#
# hypo = X*W
# cost = tf.reduce_mean(tf.square(hypo-Y))
#
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
#
# ##opti = tf.train.GradientDescentOptimizer(learning_rate=0.01) \ # train = opti.minimize(cost)와 같은 코드
# learning_rate = 0.1
# gradient = tf.reduce_mean((W*X-Y)*X
# descent = W - learning_rate*gradient
# update = W.assign(descent)
# ######################################################################################
#
# for step in range(21):
#     sess.run(update,feed_dict={X:Xdata,Y:Ydata}) #X,Y의 값을 feed_dict로 뿌려준뒤 그 경사면을 업데이트해준다.
#     print(step,sess.run(cost,feed_dict={X:Xdata,Y:Ydata}),sess.run(W))

#################################cost를 최소화 시키는 방법##########################3#########
#cost를 최대한 0으로 만드는 알고리즘이 Gradient descent알고리즘임-> cost를 최소화시킴, 경사도에 따라 한발한발 움직인다고 생각
#경사도를 구할때는 미분을 사용->미분한다는 말이 한 그래프의 점에서 기울기를 구한다고생각하면 됨. LinearRegression을 적용할때, cost(W,b)가 반ㄷ느시 Convex Fuction(밥그릇을 뒤집어놓은듯한 모양)이여야한다.
#지금 간단하게  보기위해서 b를 뱬 H(x) = Wx로 보겠다. 그럼 cost(W) = 1/m*시그마m까지*(W*x-y)^2 가되는데 이때 cost가 최소화되는 W를 찾자
# import tensorflow as tf
# import pandas.matplotlib.pyplot as plt
#
# X = [1,2,3]
# Y = [1,2,3]
#
# W = tf.placeholder(tf.float32)#placeholder로 만든 이유는 값이 어떻게되는지 우리가 임의대로 바꿔가면서 보겠다.
# hypo = X*W
# cost = tf.reduce_mean(tf.square(hypo-Y))
#
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
# W_val = [] #그래프를 그리기위한 배열
# cost_val=[] #그래프를 그리기위한 배열
# for i in range(-30,50):#이만큼 움직이면서
#     feed_W = i*0.1 #i가 돌때마다 feed_W값이 할당되고 그 값이 아래 feed_dict에서 뿌려진다.
#     curr_cost,curr_W=sess.run([cost,W],feed_dict={W:feed_W}) #객체를 만들어서 그래프 그려줄 객체에 넣어줌
#     W_val.append(curr_W)#만들어준 배열에 넣어줌
#     cost_val.append(curr_cost)
# plt.plot(W_val,cost_val) #matplotlib으로 그려줌, W가 x축, cost가 Y축인 그래프를 만들어줌
# plt.show()# 그래프에서 W가 어떠한 지점에있을때,W가 +방향쪽인지 -방향쪽인지도 알아야한다.
# #W = W - (cost함수를 미분한값) :이게 Gradient Descent알고리즘이며 이런식으로 우리가 W값을 조정한다라고 생각하면됌.
# # #이것을 코드로 표현하면 이런식인데
# # learning_rate = 0.1
# # gradient = tf.reduce_mean((W*X-Y)*X)
# # descent = W - learning_rate*gradient
# # update = W.assign(descent) #assign :맡기다.즉 W가 업데이트됨
# #이런식으로 나타낼수있는데 opti = tf.train.GradientDescentOptimizer(learning_rate=0.01) \ # train = opti.minimize(cost) 이 함수를 수동적으로 풀어쓴것이라 생각하면됨.