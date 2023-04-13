<p><a href="https://www.beecrowd.com.br/repository/UOJ_2609_en.html">beecrowd.com.br/repository/UOJ_2609_en.html</a></p><hr>
                                  <div>
                                    <span>URI Online <strong>SQL</strong> | 2609 </span>
                                    <h1>Products by Categories</h1>
                                    <div>
                                      <p>Paulo R. Rodegheri <img src="https://resources.beecrowd.com.br/gallery/images/flags/br.gif" alt="BR"> Brasil</p>
                                    </div>
                                    <strong>Timelimit: 1</strong>
                                  </div>
                                  <div>
                                  <div>
                                    <p>As usual the sales industry is doing an analysis of how many products we have in stock, and you can help them.</p>
                                    <p>Then your job will display the name and amount of products of each category.</p>
                                  </div>
                                  <div>
                                  <h2>Schema</h2>
                                  <div>
                                  <table>
                                  <caption>products</caption>
                                  <tbody><tr>
                                  <td><strong>Column</strong></td>
                                  <td><strong>Type</strong></td>
                                </tr>
                                <tr>
                                  <td>id (PK)</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>name</td>
                                  <td>varchar</td>
                                </tr>
                                <tr>
                                  <td>amount</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>price</td>
                                  <td>numeric</td>
                                </tr>
                                <tr>
                                  <td>id_categories (FK)</td>
                                  <td>numeric</td>
                                </tr>
                              </tbody></table>
                              <table>
                              <caption>categories</caption>
                              <tbody><tr>
                              <td><strong>Column</strong></td>
                              <td><strong>Type</strong></td>
                            </tr>
                            <tr>
                              <td>id (PK)</td>
                              <td>numeric</td>
                            </tr>
                            <tr>
                              <td>name</td>
                              <td>varchar</td>
                            </tr>
                          </tbody></table>
                        </div>
                      </div>
                      <div>
                      <h2>Tables</h2>
                      <div>
                      <table>
                      <caption>products</caption>
                      <tbody><tr>
                      <td><strong>id</strong></td>
                      <td><strong>name</strong></td>
                      <td><strong>amount</strong></td>
                      <td><strong>price</strong></td>
                      <td><strong>id_categories</strong></td>
                    </tr>
                    <tr>
                      <td>1</td>
                      <td>Two-doors wardrobe</td>
                      <td>100</td>
                      <td>800</td>
                      <td>1</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>Dining table</td>
                      <td>1000</td>
                      <td>560</td>
                      <td>3</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td>Towel holder</td>
                      <td>10000</td>
                      <td>25.50</td>
                      <td>4</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td>Computer desk</td>
                      <td>350</td>
                      <td>320.50</td>
                      <td>2</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td>Chair</td>
                      <td>3000</td>
                      <td>210.64</td>
                      <td>4</td>
                    </tr>
                    <tr>
                      <td>6</td>
                      <td>Single bed</td>
                      <td>750</td>
                      <td>460</td>
                      <td>1</td>
                    </tr>
                  </tbody></table>
                  <table>
                  <caption>categories</caption>
                  <tbody><tr>
                  <td><strong>id</strong></td>
                  <td><strong>name</strong></td>
                </tr>
                <tr>
                  <td>1</td>
                  <td>wood</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>luxury</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>vintage</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>modern</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>super luxury</td>
                </tr>
              </tbody></table>
            </div>
          </div>
          <div>
          <h2>Output Sample</h2>
          <div>
          <table>
          <tbody><tr>
          <td><strong>name</strong></td>
          <td><strong>sum</strong></td>
        </tr>
        <tr>
          <td>luxury</td>
          <td>350</td>
        </tr>
        <tr>
          <td>modern</td>
          <td>13000</td>
        </tr>
        <tr>
          <td>wood</td>
          <td>850</td>
        </tr>
        <tr>
          <td>vintage</td>
          <td>1000</td>
        </tr>
      </tbody></table>
    </div>
  </div>
  <p>
  </p>
</div>