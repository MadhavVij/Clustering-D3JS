from flask import Flask, render_template, request
import os
import time

from pylab            import plot,show
from numpy            import vstack,array
from numpy.random     import rand
from scipy.cluster.vq import kmeans, vq, whiten
import csv
app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template('index.html')


port = os.getenv('PORT', '80')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))


@app.route('/clustering/')
@app.route('/clustering/<int:K>')
def cluster(K=3):

    start_time = time.time()
    dataVal = []
    clustVal = []

    with open('/home/ubuntu/quiz5/input/data2.csv', 'rb') as f:
        reader = csv.reader(f)
        for idx,row in enumerate(reader):
            if idx > 0:
                dataVal.append([float(val) for val in row[10:]])
                clustVal.append([row[3]])

    data = vstack(dataVal)
    clust = vstack(clustVal)

    data = whiten(data)

    centroids, distortion = kmeans(data, K)
    print(f"distortion = {str(distortion)}")


    idx, _ = vq(data, centroids)

    print(clust)
    print(data)

    numb = []

    for i in range(K):
        result_names = clust[idx == i, 0]
        print("=================================")
        print(f"Cluster {str(i + 1)}")
        clus_name = f"Cluster {str(i + 1)}"
        count = 0
        for name in result_names:
            print(name)
            count += 1
        #numb.append((clus_name,count))
        numb.append(count)
    print(sorted(numb))
    end_time = time.time()
    numb = sorted(numb,reverse=True)
    numb.append(start_time)
    numb.append(end_time)

    return render_template('barchart.html', numb=numb)



###################################################################

@app.route('/display')
def dispCluster(K=6):

    start_time = time.time()
    dataVal = []
    clustVal = []

    with open('/home/ubuntu/quiz5/input/data2.csv', 'rb') as f:
        reader = csv.reader(f)
        for idx,row in enumerate(reader):
            if idx > 0:
                dataVal.append([float(val) for val in row[9:]])
                clustVal.append([row[3]])

    data = vstack(dataVal)
    clust = vstack(clustVal)

    data = whiten(data)

    centroids, distortion = kmeans(data, K)



    idx, _ = vq(data, centroids)

    print(f'clust = {str(clust)}')
    print(f'data = {str(data)}')

    numb = []

    for i in range(K):
        result_names = clust[idx == i, 0]

        count = 0
        for name in result_names:
            print(name)
            count += 1

        numb.append(count)

    end_time = time.time()
    numb = sorted(numb,reverse=True)
    numb.append(start_time)
    numb.append(end_time)
    numb.append(centroids)

    return render_template('display.html', numb=numb)


####################################################################


@app.route('/process',methods=['POST','GET'])
def ClusterInfo():
    start_time = time.time()
    numb = []
    if request.method == 'POST':
        col1 = request.form['col1']
        col2 = request.form['col2']
        K = int(request.form['number1'])

        dataVal = []
        clustVal = []

        with open('/home/ubuntu/quiz5/input/data2.csv', 'rb') as f:
            reader = csv.reader(f)
            for idx,row in enumerate(reader):
                if idx > 0:
                    dataVal.append([float(val) for val in row[9:]])
                    clustVal.append([row[3]])

        data = vstack(dataVal)
        clust = vstack(clustVal)

        data = whiten(data)

        centroids, distortion = kmeans(data, K)



        idx, _ = vq(data, centroids)

        print(f'clust = {str(clust)}')
        print(f'data = {str(data)}')



        for i in range(K):
            result_names = clust[idx == i, 0]

            for name in result_names:
                print(name)
                numb.append(name)

        numb = sorted(numb)
        numb.append(centroids)
    end_time = time.time()

    numb.append(start_time)
    numb.append(end_time)


    return render_template('display.html', number1=numb)


######################################################################

@app.route('/pie',methods=['POST','GET'])
def clusterPie():
    numb = []
    if request.method == 'POST':
        col1 = request.form['col1']
        col2 = request.form['col2']
        K = int(request.form['number1'])

        dataVal = []
        clustVal = []

        with open('/home/ubuntu/quiz5/input/data2.csv', 'rb') as f:
            reader = csv.reader(f)
            for idx,row in enumerate(reader):
                if idx > 0:
                    dataVal.append([float(val) for val in row[9:]])
                    clustVal.append([row[3]])

        data = vstack(dataVal)
        clust = vstack(clustVal)

        data = whiten(data)

        centroids, distortion = kmeans(data, K)
        print(f"distortion = {str(distortion)}")


        idx, _ = vq(data, centroids)

        print(clust)
        print(data)

        numb = []

        for i in range(K):
            result_names = clust[idx == i, 0]
            print("=================================")
            print(f"Cluster {str(i + 1)}")
            clus_name = f"Cluster {str(i + 1)}"
            count = 0
            for name in result_names:
                print(name)
                count += 1
            numb.append(count)


    return render_template('piechart.html', numb=numb)

###################################################################

@app.route('/bar',methods=['POST','GET'])
def clusterBar():
    numb = []
    if request.method == 'POST':
        col1 = request.form['col1']
        col2 = request.form['col2']
        K = int(request.form['number1'])

        dataVal = []
        clustVal = []

        with open('/home/ubuntu/quiz5/input/data2.csv', 'rb') as f:
            reader = csv.reader(f)
            for idx,row in enumerate(reader):
                if idx > 0:
                    dataVal.append([float(val) for val in row[9:]])
                    clustVal.append([row[3]])

        data = vstack(dataVal)
        clust = vstack(clustVal)

        data = whiten(data)

        centroids, distortion = kmeans(data, K)
        print(f"distortion = {str(distortion)}")


        idx, _ = vq(data, centroids)

        print(clust)
        print(data)

        numb = []

        for i in range(K):
            result_names = clust[idx == i, 0]
            print("=================================")
            print(f"Cluster {str(i + 1)}")
            clus_name = f"Cluster {str(i + 1)}"
            count = 0
            for name in result_names:
                print(name)
                count += 1
            numb.append(count)


    return render_template('barchart.html', numb=sorted(numb,reverse=True))