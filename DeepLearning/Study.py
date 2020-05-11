#################################Linear Regression#######################
#아래 문제와 같지만  x,y값을 저런식으로 바로 선언해주지않고, 필요할때 넣어주는 placeholde안에 넣어줌
# import tensorflow as tf
# x = tf.placeholder(tf.float32,shape = [None])#shape에서 []이건 1차원이란거고 None은 아무값이,몇개든 들어올수있다.
# y = tf.placeholder(tf.float32)
#
# W = tf.Variable(tf.random_normal([1]))
# b = tf.Variable(tf.random_normal([1]))
# hp = x * W + b
#
# cost = tf.reduce_mean(tf.square(hp-y))
#
# opti = tf.train.GradientDescentOptimizer(learning_rate=0.01)
# train = opti.minimize(cost)
#
# sess = tf.Session()
# sess.run(tf.global_variables_initializer())
#
# for i in range(0,2001):
#     cost_var,W_var,b_var,_=sess.run([cost,W,b,train],feed_dict={x:[1,2,3,4,5],y:[2.1,3.1,4.1,5.1,6.1]})#train안에 cost,hp가 다있으므로 cost,W,b다 알려주고거기에 feed_dict한다
#     if i % 20 ==0:
#         print(i,sess.run([cost,W,b,train],feed_dict={x:[1,2,3,4,5],y:[2.1,3.1,4.1,5.1,6.1]}))
#
# print(sess.run(hp,feed_dict={x:[5]})) #이건 y = x + 1.1 로 그려진 그래프를 테스트해보는것.어차피 W,b는 위에서 train했으므로 x값만 주면됨
# print(sess.run(hp,feed_dict={x:[2.5]}))
# print(sess.run(hp,feed_dict={x:[1.5,3.5]}))
#1.H(x)= W*x+b와 cost에 해당하는 함수를 만듦,2.그담에 feed_dict를 이용하여 x와 y데이터 던져줌 3.내부적으로 W,b를 업데이트 시켜줌->그담에 우리가 테스트해볼겸 H(x)만갖고와서 출력해봄


#문제풀때 그래프를 직접 그려보면서 할것
#보통 Linear Regression에 가장 많이 쓰는 공식 : H(x)= Wx+b 라는 1차방정식 사용함,여기서 H(x)는 우리가 대충 맞춰보기떄문에 가설이라고 볼 수 잇다. 보통 대충 알아볼때 0부터 각각 대입해봐서 어느정도 식을 구해본다
#우리가 대충 만들어본 1차방정식과 실제 y값과의 차이를 cost,Loss(손실) 라고 부르는데 당연히 H(x)-y의 제곱을 함.뭐 양수일수도 음수일수도 있으니까, 아무튼 이 cost가 적어야지 확실한거
#아무튼 H(x)-y의 제곱을 한거를 싹 다 더하고 평균 내줌 이게 바로 cost Function->그 갯수가 엄청 많을수도 있으므로 cost = 1/m*시그마 m까지((H(xi)-yi))^2
#즉 그렇게 되면 어차피 H(x)에서 y를 뺌으로 가장 중요한건 W,b인거,그래서 cost를 가장 작게 만들어주는 애들을 찾아야하는게 Linear Regression,그래서 cost는W,b가 어떤값이냐에 따라 cost가 커질수도 또는 작아질수도
# import tensorflow as tf
# x = [1,2,3,4]
# y = [5,7,8,11 ]
# W = tf.Variable(tf.random_normal([1]))  #이 변수의 shape을 정해줘야함 그래서 W,b값을 모르니까 random값 준거,그때쓰는 함수인듯 그때 주는 값이 값1개인 1차원 배열 줘서 [1]이렇게 표시한거,변수,name은 걍 쓴거
# b = tf.Variable(tf.random_normal([1])) #Varible은 우리가사용하는게 아니라 tensorflow가 사용하는애이다. tensorflow가 자체적으로 바꾸는 값이다.즉 tensorflow가 학습하는 과정에서 자기가 변경을 시켜주는 값이다.
# hp = x * W + b #그래프를 말해준다. H(x) = W*x+b -> 얘 노드임
#
# cost =  tf.reduce_mean(tf.square(hp-y))#square은 제곱 파이썬 함수,reduce_mean은 평균알려주는 함수
# ##이 아래가 cost 값 줄여주는거
# opti = tf.train.GradientDescentOptimizer(learning_rate=0.01) #0.01만큼 움직이면서 배운다.GradientDescent =경사하강
# train = opti.minimize(cost) #minimize함수를 호출해서 cost를 최소화하라는말, 그럼 W,b를 지가 조정함,얘도 노드임
# #이 train이란 노드에 cost가 연결이되어있고,cost한테 hp가 연결되어있고, hp한텐 W,b가 연결되어있다는거,그래서 train을 시켜주면 W,b가 조정이됨
# sess = tf.Session()
# sess.run(tf.global_variables_initializer()) #이건 variable실행하기전엔 반드시 실행해줘야하는 놈,즉 초기화를 해주는거
#
# for i in range(0,2001):
#     sess.run(train) #쉽게 생각하면 학습시켜주는거
#     if i % 20 ==0:
#         print(i,sess.run(cost),sess.run(W),sess.run(b)) #맨첨에 W,b값은 위에 만들어줌 shape 1차원의 랜덤값임


#######################################################################################################
#가장먼저 우리가 노드를 만들어줌, 그게 나중에 모이면 그래프가 됨 ->그 담에 Session()으로 작동시켜주는 애 만듬->그담 작동
#placeholder(데이터타입):값을 저장하는 일종의 통(버킷)이고,필요할때 값을 던져주는것, feed_dict={a:3,b:5}는 통 채워주는애로 생각
# tf.int32,tf.float32 젤 많이 사용 , tf.constant(3.0,데이터 타입) = constant는 상수
# rank = 몇차원이냐 = [1,2,3,4] 는 1차원  [[1,2],[3,4]]는 2차원 그냥 int arr[2][2] 생각
#shape = [[1,2,3],[4,5,6],[7,8,9]]는 shape = [3,3] 즉 3행 3열 즉 int arr[3][3]로 생각, 괄호치는 애들은
# 위부터 아래로 정렬된다고 생각하면 됨.
# import tensorflow as tf
#
# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adderNode = a+b
#
# sess= tf.Session()
#
# print(sess.run(adderNode,feed_dict={a:3,b:4.5}))
# print(sess.run(adderNode,feed_dict={a:[1,3],b:[2,4]}))

