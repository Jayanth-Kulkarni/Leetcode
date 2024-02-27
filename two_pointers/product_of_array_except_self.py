def product_except_self(arr):
    left,right = 0,len(arr)-1
    prefix_product,postfix_product=[],[]
    prefix,postfix=1,1
    while left<=len(arr)-1 and right>=0:
        prefix *= arr[left]
        postfix *= arr[right]
        prefix_product.append(prefix)
        postfix_product.append(postfix)
        left+=1
        right-=1
    postfix_product = postfix_product[::-1]
    prefix_product.insert(0,1)
    postfix_product.insert(len(postfix_product),1)
    result = []
    for idx,i in enumerate(arr):
        result.append(prefix_product[idx]*postfix_product[idx+1])
    return result

product_except_self([3,-1,-3,2,1,-2])